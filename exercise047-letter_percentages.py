# Napisz funkcję, która przyjmie tekst i zwróci słownik, w którym:
# klucze to litery (znormalizowane),
# wartości to procent (od 0 do 100) wystąpień danej litery spośród wszystkich liter.
def letter_percentages(text: str) -> dict[str, float]:
    letters_frequency = {}
    
    for char in text:
        if char.isalpha():
            char = char.lower()
            letters_frequency[char] = letters_frequency.get(char, 0) + 1

    letters_sum = sum(letters_frequency.values())

    for element in letters_frequency:
            value = letters_frequency[element]
            letters_frequency[element] = round(value/letters_sum*100, 1)
    return letters_frequency

print(letter_percentages("abAac"))