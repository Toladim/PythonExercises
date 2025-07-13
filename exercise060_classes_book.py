# Napisz klasę Book, która:
# W konstruktorze (__init__) przyjmuje:
# title – tytuł książki,
# opcjonalnie authors – listę autorów (domyślnie pustą).
# Przechowuje oba te atrybuty jako self.title i self.authors.
# Ma metodę add_author(author_name: str), która dodaje autora do listy.
# Ma metodę describe(), która zwraca:
# "Book: [title] by [author1, author2]" – jeśli autorzy istnieją,
# "Book: [title] (no authors listed)" – jeśli brak autorów.
class Book:
    def __init__(self, title, authors=None):
        self.title = title
        self.authors = [] if authors is None else authors

    def add_author(self, author_name: str):
        self.authors.append(author_name)

    def describe(self):
        if not self.authors:
            return f"Book: {self.title} (no authors listed)"
        else:
            return f"Book: {self.title} by {', '.join(self.authors)}"

b = Book("The Pragmatic Programmer")
print(b.describe())
b.add_author("Andrew Hunt")
b.add_author("David Thomas")
print(b.describe())