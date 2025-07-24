# Napisz funkcję, która zlicza liczbę samogłosek w podanym łańcuchu.
# Przykład wywołania: vowels_count("Abrakadabra") Wynik: 5
def vowels_count(text: str) -> int:
    vowels= "aeiouy"
    return sum(1 for letter in text if letter.lower() in vowels)
    

print(vowels_count("Abrakadabra"))