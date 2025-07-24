# Napisz funkcję, która zlicza, ile razy dany znak występuje w łańcuchu.
# Przykład wywołania: count_char("hello world", "l") Wynik: 3
def count_char(text: str, letter: str) -> int:
    return text.count(letter)

print(count_char("hello world", "l"))