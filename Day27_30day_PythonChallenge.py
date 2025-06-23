from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Database Setup
DATABASE_URL = "sqlite:///./books.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy Model
class BookDB(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(String, nullable=True)

# Create the database table
Base.metadata.create_all(bind=engine)

# Pydantic Schema
class Book(BaseModel):
    title: str
    author: str
    description: str = ""

model_config = {
    "from_attributes": True
}

class BookResponse(Book):
    id: int

# FastAPI App
app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Book
@app.post("/books/", response_model=BookResponse)
def create_book(book: Book, db: Session = Depends(get_db)):
    db_book = BookDB(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Get All Books
@app.get("/books/", response_model=List[BookResponse])
def read_books(db: Session = Depends(get_db)):
    books = db.query(BookDB).all()
    return books

# Get Book by ID
@app.get("/books/{book_id}", response_model=BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

# Update Book
@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: Book, db: Session = Depends(get_db)):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db_book.title = book.title
    db_book.author = book.author
    db_book.description = book.description

    db.commit()
    db.refresh(db_book)
    return db_book

# Delete Book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}
