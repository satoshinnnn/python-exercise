# Library system

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"{self.title} {self.author}")

class Library:  # adopt aggregation
    def __init__(self):
        self.books = []  #books ís a list that appended by object book1, book2, book3

    def add_book(self, book):  # append books to library (with book is parameter)
        self.books.append(book)

    def show_books(self):
        for book in self.books:  # 'book' in this case just is a Local Variable and "books" is a list that represents (includes) objects book1, book2 and book3
            print(f"{book.title} {book.author}")

class Librarycard:  # adopt composition
    def __init__(self, holder_name, book_name):
        self.holder_name = holder_name
        self.book_name = book_name   # directly assign the Book object to the card
    def borrow(self):
        print(f"{self.holder_name} borrowed the book {self.book_name.title}")

# create object for class Book
book1 = Book("Crayon Shin-chan", "Yoshito Usui")
book2 = Book("Dragon Ball", "Akira Toriyama")
book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")

# Append object from class Book to class Library
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# create object for class Library (declare parameter cho holder_name và book_name with filling directly book object)
librarycard1 = Librarycard("Bao Khanh", book1)
librarycard2 = Librarycard("Bao Khanh", book2)
librarycard3 = Librarycard("Bao Khanh", book3)

# Test borrow, display info,...
