# Napisz funkcję, która zlicza liczbę słów w podanym zdaniu.
# Przykład wywołania: count_words("Ala ma kota") Wynik: 3
def count_words(text: str) -> int:
    return len(text.split())

print(count_words("Ala ma kota"))