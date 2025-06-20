from dataclasses import dataclass

# Dataclass used to store the book details.
@dataclass
class library_book():
    title: str
    author: str
    isbn_number: str
    publication_year: str

# Method to display book details
    def display_details(self): 
        print("📚 Book Details:")
        print(f"• Title            : {self.title}")
        print(f"• Author           : {self.author}")
        print(f"• ISBN Number      : {self.isbn_number}")
        print(f"• Publication Year : {self.publication_year}")

# creating instance for dataclass

atomic_habits = library_book(title="Python", author="Dr. Nageshwara Rao", isbn_number="978-32456897123", publication_year="2015") 
# Display the book details
atomic_habits.display_details() 