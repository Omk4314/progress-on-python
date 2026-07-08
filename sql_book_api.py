from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional

SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind = engine)
Base = declarative_base()

class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, index = True)
    author = Column(String)
    price = Column(Float)
    isbn = Column(String)
Base.metadata.create_all(bind=engine)

class Book(BaseModel):
    title: str = Field(min_length = 1, max_length = 100)
    author: str
    price: float = Field(gt = 0)
    isbn: str = Field(pattern = r"^\d{13}$")

    class Config:
        from_attributes = True


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def create_book(book: Book, db: Session = Depends(get_db)):
    db_book = BookModel(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {"message": f"Created '{db_book.title}' by {db_book.author}", "id": db_book.id}

@app.get("/books/")
def read_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()
    return books

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail = "Book Not Found!")
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code = 404, detail = "Book Not Found!")
    db_book.title = book.title
    db_book.author = book.author
    db_book.price = book.price
    db_book.isbn = book.isbn
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code = 404, detail = "Book Not Found!")
    db.delete(db_book)
    db.commit()
    return {"message": f"Book {book_id} deleted"}
