from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str
    price: float = Field(gt=0, description="Must be positive")
    isbn: str = Field(pattern=r"^\d{13}$")

book_db = []
next_id = 1

# --- CREATE ---
@app.post("/books/")
def create_book(book: Book):
    global next_id
    book_dict = book.model_dump()
    book_dict["id"] = next_id
    next_id += 1
    book_db.append(book_dict)
    return {"message": f"Created '{book.title}' by {book.author}", "id": book_dict["id"]}

# --- READ ALL / SEARCH ---
@app.get("/books/")
def read_books(title: Optional[str] = None):
    if title:
        for book in book_db:
            if book["title"] == title:
                return book
        raise HTTPException(status_code=404, detail="Book not found")
    return book_db

# --- READ ONE ---
@app.get("/books/{book_id}")
def read_book(book_id: int):
    for book in book_db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book {book_id} not found")

# --- UPDATE (PUT) ---
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for i, existing in enumerate(book_db):
        if existing["id"] == book_id:
            updated = book.model_dump()
            updated["id"] = book_id
            book_db[i] = updated
            return {"message": f"Updated book {book_id}", "book": updated}
    raise HTTPException(status_code=404, detail=f"Book {book_id} not found")

# --- DELETE ---
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(book_db):
        if book["id"] == book_id:
            removed = book_db.pop(i)
            return {"message": f"Deleted book {book_id}", "book": removed}
    raise HTTPException(status_code=404, detail=f"Book {book_id} not found")