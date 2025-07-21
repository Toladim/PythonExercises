# Napisz funkcję, która sprawdza, czy lista jest posortowana rosnąco.
# Przykład wywołania: is_sorted([1, 2, 5, 4]) Wynik: False
def is_sorted(nums: list[int]) -> bool:
    return nums == sorted(nums)

print(is_sorted([1, 2, 5, 4]))