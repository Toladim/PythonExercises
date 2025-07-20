# Napisz funkcję, która znajduje minimalny element w liście liczb.
# Przykład wywołania: minimum([5, 1, 9, 3]) Wynik: 1

def minimum(nums: list[int]) -> int:
    return min(nums)

print(minimum([5, 1, 9, 3]))