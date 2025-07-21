# Napisz funkcję, która rozdziela listę liczb na dwie listy: 
# jedną z liczbami parzystymi i drugą z nieparzystymi.
# Przykład wywołania: divide_to_even_and_odd([1, 2, 3, 4, 5]) Wynik: ([2, 4], [1, 3, 5])

def divide_to_even_and_odd(nums: list[int]) -> tuple[list[int], list[int]]:
    even, odd = [], []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd
    

print(divide_to_even_and_odd([1, 2, 3, 4, 5]))