# Napisz funkcję, która usuwa wszystkie samogłoski z łańcucha.
# Przykład wywołania: without_vowels("abcdef") Wynik: "bcdf"
def without_vowels(text: str) -> str:
    vowels= "aeiouyAEIOUY"
    return "".join(char for char in text if char not in vowels)

print(without_vowels("abcdef"))