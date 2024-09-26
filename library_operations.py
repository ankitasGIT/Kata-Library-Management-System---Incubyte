import json
import os

class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def to_dict(self):
        """Converting from book to json"""
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_available": self.is_available
        }
    
    @classmethod
    def from_dict(cls, data):
        """ Convert from json to object (book)"""
        book = cls(data["isbn"], data["title"], data["author"], data["publication_year"])
        book.is_available = data["is_available"]
        return book
    
class Library:
    def __init__(self):
        self.books = {}
        self.load_data()

    def add_book(self, book):
        """ Implementation of add_book functionality """
        if book.isbn in self.books:
            raise ValueError("Book with this ISBN already exists")
        self.books[book.isbn] = book
        self.save_data()

    def clear_all_data(self):
        """Empties all the records in the JSON file and resets the books dictionary."""
        self.books = {}
        self.save_data()

    def save_data(self):
        """ Writes entries to json file """
        with open("library_data.json", "w") as f:
            json.dump({isbn: book.to_dict() for isbn, book in self.books.items()}, f)

    def load_data(self):
        """ Loads data from json file """
        if os.path.exists("library_data.json"):
            with open("library_data.json", "r") as f:
                data = json.load(f)
                self.books = {isbn: Book.from_dict(book_data) for isbn, book_data in data.items()}