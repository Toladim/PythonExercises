# Napisz funkcję rekurencyjną, która oblicza sumę elementów listy.
# Przykład wywołania: sum_lists_rec([1, 2, 3, 4]) Wynik: 10
def sum_lists_rec(nums: list[int]) -> int:
    print(nums)
    if not nums:
        return 0
    else:   
        return nums[0] + (sum_lists_rec(nums[1:]))
                
print(sum_lists_rec([1, 2, 3, 4]))