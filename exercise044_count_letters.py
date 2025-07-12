# Napisz funkcję, która przyjmie string i zwróci słownik, w którym:
# klucze to litery (małe i wielkie traktuj jako jedno),
# wartości to liczba ich wystąpień w tekście (ignoruj spacje i znaki interpunkcyjne).
def count_letters(text: str) -> dict[str, int]:
    letters_counter = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in letters_counter:
                letters_counter[char] += 1
            else:
                letters_counter[char] = 1
    return letters_counter


print(count_letters("Hello, world!"))
