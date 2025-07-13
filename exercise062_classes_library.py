# Stwórz klasę Library, która:
# W konstruktorze (__init__) przyjmuje:
# name – nazwa biblioteki,
# opcjonalną listę książek (books), domyślnie pustą.
# Ma metodę add_book(book: Book), która dodaje obiekt książki do biblioteki.
# Ma metodę list_books(), która wypisuje wszystkie książki w formacie:
# "Library: [nazwa]"
# - 'Tytuł' by Autor
# - 'Inny tytuł' by Inny Autor
# Ma metodę find_by_author(author_name: str), która zwraca listę tytułów książek napisanych przez danego autora.
from exercise061_classes_book_2 import Book

class Library:
    def __init__(self, name, books=None):
        self.name = name
        self.books = [] if books is None else books
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def list_books(self):
        print(f"Library: {self.name}: ")
        for book in self.books:
            print(f"- {book}")

    def find_by_author(self, author_name: str) -> list[str]:
        return [book.title
                 for book in self.books
                   if any(author.lower() == author_name.lower() for author in book.authors)]

book1 = Book("1984", ["George Orwell"])
book2 = Book("Animal Farm", ["George Orwell"])
book3 = Book("Brave New World", ["Aldous Huxley"])
lib = Library("Central Library")
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.list_books()
print(lib.find_by_author("George Orwell"))