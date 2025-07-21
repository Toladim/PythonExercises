# Napisz funkcję, która odwraca kolejność elementów w liście 
# (in-place lub poprzez utworzenie nowej listy).
# Przykład wywołania: reverse_list([1, 2, 3, 4]) Wynik: [4, 3, 2, 1]
def reverse_list(nums: list[int]) -> list[int]:
    return nums[::-1]

print(reverse_list([1, 2, 3, 4]))