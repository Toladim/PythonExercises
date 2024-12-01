class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.avaible = True
    
    def borrow(self):
        if self.avaible:
            self.avaible = False
            print(f"Książka '{self.title}' została wypożyczona.")
        else:
            print(f"Książka '{self.title}' jest już wypozyczona.")
    
    def return_book(self):
        if not self.avaible:
            self.avaible = True
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
            if book.avaible:
                print(f"- {book.title} by {book.author} ({book.year})")


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