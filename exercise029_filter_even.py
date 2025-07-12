def filter_even(numbers: list[int]) -> list[int]:

    return[x for x in numbers if x%2 == 0]

print(filter_even([1, 2, 3, 4, 5, 6]))