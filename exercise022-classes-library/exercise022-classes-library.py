class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"Książka '{self.title}' została wypożyczona.")
        else:
            print(f"Książka '{self.title}' jest już wypozyczona.")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Książka '{self.title}' została zwrócona.")
        else:
            print(f"Książka '{self.title}' już była dostępna.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Dodano książkę: '{book.title}'.")
    
    def show_avaible_books(self):
        print("Dostępne książki w bibliotece:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} by {book.author} ({book.year})")
    
    def search_book(self, search):
        found = False
        for book in self.books:
            if search.lower() in book.author.lower() or search.lower() in book.title.lower():
                print(f"- {book.author} - {book.title}, ({book.year})")
                found = True
        if not found:
            print("Nie znaleziono książki pasującej do wyszukiwania.")


book1 = Book("Python dla początkujących", "Jan Kowalski", 2020)
book2 = Book("Nowa Ksiazka", "Parry Wziet", 1989)

library = Library()

library.add_book(book1)
library.add_book(book2)
library.show_avaible_books()
book1.borrow()
book1.borrow()
library.show_avaible_books()
book1.return_book()
library.show_avaible_books()
library.search_book("Pr")