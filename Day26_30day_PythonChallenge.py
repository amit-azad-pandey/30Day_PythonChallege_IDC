# Challenge Develop a FastAPI application with endpoints to manage a library 
# of books, including creating, reading, updating, and deleting books.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Book model
class Book(BaseModel):
    id: int
    title: str
    author: str

# In-memory list
books = []

# Create
@app.post("/books/")
def add_book(book: Book):
    books.append(book)
    return {"msg": "Book added"}

# Read all
@app.get("/books/")
def get_books():
    return books

# Update
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for i, b in enumerate(books):
        if b.id == book_id:
            books[i] = book
            return {"msg": "Book updated"}
    return {"msg": "Book not found"}

# Delete
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b.id == book_id:
            books.pop(i)
            return {"msg": "Book deleted"}
    return {"msg": "Book not found"}
