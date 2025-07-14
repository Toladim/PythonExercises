# Utwórz klasę LoanableLibrary, która dziedziczy po Twojej klasie Library:
# W konstruktorze:
# wywołaj super().__init__(name, books),
# zainicjalizuj atrybut borrowed: dict[str, str] jako pusty słownik.
# Dodaj metodę borrow_book(self, title: str, borrower: str):
# jeśli książka o podanym tytule jest w self.books i jeszcze nie została wypożyczona, dodaj wpis do self.borrowed[title] = borrower;
# w przeciwnym razie wyrzuć wyjątek ValueError("Book not available").
# Dodaj metodę return_book(self, title: str):
# usuń wpis title z self.borrowed, albo wyrzuć ValueError("Book was not borrowed").
# Nadpisz metodę list_books(self), aby wypisywała:
# Library: [nazwa]
#  - [tytuł] by [autorzy] (available)
#  - [tytuł] by [autorzy] (borrowed by [imię])
from exercise062_classes_library import Library

class LoanableLibrary(Library):
    def __init__(self, name, books=None):
        super().__init__(name, books)
        self.borrowed: dict[str, str] = {}
    
    def borrow_book(self, title: str, borrower: str):
        if title in self.books and title not in self.borrowed:
            self.borrowed[title] = borrower
        # else:
        #     Exception ValueError("Book not available")
   