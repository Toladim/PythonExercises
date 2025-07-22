# Napisz funkcję, która sprawdza, czy dwie listy mają takie same elementy 
# (niekoniecznie w tej samej kolejności).
# Przykład wywołania: is_lists_same([1, 2, 3], [3, 1, 2]) Wynik: True

def is_lists_same(list1: list[int], list2: list[int]) -> bool:
    
    return sorted(list1) == sorted(list2)

print(is_lists_same([1, 2, 3], [3, 1, 2]))