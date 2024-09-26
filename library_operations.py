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

    def borrow_book(self, isbn):
        """Implementation of borrow_book operation"""
        if isbn not in self.books:
            raise ValueError("Book not found")
        if not self.books[isbn].is_available:
            raise ValueError("Book is not available")
        self.books[isbn].is_available = False
        self.save_data()

    def return_book(self, isbn):
        """Implementation of return_book operation"""
        if isbn not in self.books:
            raise ValueError("Book not found")
        if self.books[isbn].is_available == True:
            raise ValueError("Book already returned")
        self.books[isbn].is_available = True
        self.save_data()

    def get_available_books(self):
        return [book for book in self.books.values() if book.is_available]

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

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            year = input("Enter Publication Year: ")
            try:
                book = Book(isbn, title, author, int(year))
                library.add_book(book)
                print("Book added successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            isbn = input("Enter ISBN of the book to borrow: ")
            try:
                library.borrow_book(isbn)
                print("Book borrowed successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            isbn = input("Enter ISBN of the book to return: ")
            try:
                library.return_book(isbn)
                print("Book returned successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            available_books = library.get_available_books()
            if available_books:
                print("Available Books:")
                for book in available_books:
                    print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}")
            else:
                print("No books available.")

        elif choice == "5":
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


#isbn - unique id
if __name__ == "__main__":
    main()
