# Napisz funkcję count_occurrences(),
# która przyjmie listę liczb całkowitych i zwróci słownik (dict) pokazujący,
# ile razy każda liczba wystąpiła w tej liście.

def count_occurrences(numbers: list[int]) -> dict[int, int]:
    return {x: numbers.count(x) for x in set(numbers)}

print(count_occurrences([1, 2, 2, 3, 1, 2, 4]))