# Napisz funkcję rekurencyjną, która znajduje maksymalny element w liście.
# Przykład wywołania: max_rec([7, 2, 9, 4]) Wynik: 9

def max_rec(nums: list[int]) -> int:
    if  len(nums) == 1:
        return nums[0]
    rest_max = max_rec(nums[1:])
    return nums[0] if nums[0] > rest_max else rest_max

print(max_rec([7, 2, 9, 4]))