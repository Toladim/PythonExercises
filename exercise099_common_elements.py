# Napisz funkcję, która zwraca listę elementów występujących jednocześnie w obu listach 
# (część wspólna list).
# Przykład wywołania: common_elements([1, 2, 3, 4], [3, 4, 5]) Wynik: [3, 4]
def common_elements(list1: list[int], list2: list[int]) -> list[int]:
    return list(set(list1) & set(list2))

print(common_elements([1, 2, 3, 4], [3, 4, 5]))