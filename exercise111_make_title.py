# Napisz funkcję, która kapitalizuje (zamienia na wielkie litery) 
# pierwszą literę każdego słowa w zdaniu (tzw. tytułowanie tekstu).
# Przykład wywołania: make_title("jan kowalski") Wynik: "Jan Kowalski"
def make_title(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split())

print(make_title("jan kowalski"))
