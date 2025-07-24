# Napisz funkcję, która zwraca listę elementów, które są w pierwszej liście, ale nie ma ich w drugiej 
# (różnica zbiorów reprezentowanych przez listy).
# Przykład wywołania: lists_difference([1, 2, 3, 4], [2, 4, 6]) Wynik: [1, 3]
def lists_difference(list1: list[int], list2: list[int]) -> list[int]:
    return list(set(list1) - set(list2))

print(lists_difference([1, 2, 3, 4], [2, 4, 6]))
