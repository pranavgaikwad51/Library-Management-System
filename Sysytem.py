# Project 1: Library Management System

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                print(f"Borrowed: {book}")
                return
        print("Book not available.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.available = True
                print(f"Returned: {book}")
                return
        print("Invalid return.")

# Example usage
if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("Python Basics", "Alice", "101"))
    lib.add_book(Book("Learn OOP", "Bob", "102"))
    lib.show_available_books()
    lib.borrow_book("101")
    lib.show_available_books()
    lib.return_book("101")
    lib.show_available_books()
