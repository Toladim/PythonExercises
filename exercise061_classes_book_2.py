# Uzupełnij klasę Book, aby:
# Zaimplementować metodę __str__(), która zwraca:
# "'[tytuł]' by [autor1, autor2]"
# — albo jeśli brak autorów:
# "'[tytuł]' (no authors listed)"
# Zaimplementować metodę __eq__(), która sprawdza, czy:
# title jest taki sam,
# i lista autorów taka sama (kolejność może się liczyć lub nie – Ty decydujesz!).
class Book:
    def __init__(self, title, authors=None):
        self.title = title
        self.authors = [] if authors is None else authors

    def __str__(self):
        return f"{self.title} by {', '.join(self.authors)}" if self.authors else f"{self.title} by (no authors listed)"
    
    def __eq__(self, other):
        return (self.title == other.title and
                self.authors == other.authors
                )

    def add_author(self, author_name: str):
        self.authors.append(author_name)
        
book1 = Book("1984")
book2 = Book("1984")
book2.add_author("George Orwell")

print(book1)  
print(book2)  
print(book1 == book2)  
book1.add_author("George Orwell")
print(book1 == book2)
