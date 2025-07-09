# Napisz funkcję, która przyjmie tekst i zwróci listę liter, posortowaną od najczęstszej do najrzadszej
# (znów: ignoruj wielkość liter, pomiń znaki niebędące literami).
def sort_letters_by_frequency(text: str) -> list[str]:
    letters_frequency= {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letters_frequency[char] = letters_frequency.get(char, 0) + 1
    return sorted(letters_frequency,key=letters_frequency.get, reverse=True)

print(sort_letters_by_frequency("Hello, world!"))