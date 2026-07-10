from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean  # Added Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime, timedelta

SECRET_KEY = "G7pxwL9"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    price = Column(Float)
    isbn = Column(String)

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String)
    full_name = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str
    price: float = Field(gt=0)
    isbn: str = Field(pattern=r"^\d{13}$")

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def seed_user():
    db = SessionLocal()
    user = db.query(UserModel).filter(UserModel.username == "johndoe").first()
    if not user:
        db_user = UserModel(
            username="johndoe",
            email="johndoe@gmail.com",
            full_name="John Doe",
            hashed_password=pwd_context.hash("secret"),
            disabled=False
        )
        db.add(db_user)
        db.commit()
    db.close()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Session, username: str):
    db_user = db.query(UserModel).filter(UserModel.username == username).first()  # Fixed indentation
    if db_user:
        return UserInDB(
            username=db_user.username,
            email=db_user.email,
            full_name=db_user.full_name,
            disabled=db_user.disabled,
            hashed_password=db_user.hashed_password
        )
    return None

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)  # Fixed: was missing
        user = get_user(db, username=token_data.username)
        if user is None:
            raise credentials_exception
        return user
    except JWTError:  # Fixed: was missing except block
        raise credentials_exception

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,  # Fixed: was "staus_code"
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/books/")
def create_book(book: Book, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {"message": f"Created '{db_book.title}' by {db_book.author}", "id": db_book.id}

@app.get("/books/")
def read_books(db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    books = db.query(BookModel).all()
    return books

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book Not Found!")
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book Not Found!")
    db_book.title = book.title
    db_book.author = book.author
    db_book.price = book.price
    db_book.isbn = book.isbn
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book Not Found!")
    db.delete(db_book)
    db.commit()
    return {"message": f"Book {book_id} deleted"}
