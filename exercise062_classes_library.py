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

# part 2:
# Dodaj do klasy Library metodę:
# sort_books_by_title()
# Która zwraca listę książek posortowaną alfabetycznie po tytule
# (domyślnie nie musisz uwzględniać wielkości liter, ale możesz).

# part 3:
# Dodaj do klasy Library metodę:
# sort_books_by_author(self) -> list[Book]
# ktora, zwraca książki posortowane alfabetycznie wg pierwszego autora na liście book.authors
# jeśli lista autorów jest pusta → traktuj jako "" (pusty string)

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
 
    def sort_books_by_title(self) -> list[str]:
        return sorted([book.title for book in self.books],key=str.lower)
    
    def sort_books_by_author(self) -> list[Book]:
        return sorted(self.books, key=lambda book: book.authors[0].lower() if book.authors else "")
book1 = Book("1984", ["George Orwell"])
book2 = Book("Animal Farm", ["George Orwell"])
book3 = Book("Brave New World", ["Aldous Huxley"])
book4 = Book("aazzz")
lib = Library("Central Library")
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_book(book4)
lib.list_books()
print(lib.find_by_author("George Orwell"))
print(lib.sort_books_by_title())

sorted_books = lib.sort_books_by_author()

for b in sorted_books:
    print(b)