# Napisz funkcję, która zlicza, ile w danej liście jest liczb parzystych i nieparzystych.
# Przykład wywołania: even_and_odd([1, 2, 3, 4, 5]) Result: Even: 2, Odd: 3

def even_and_odd(nums: list[int]) -> str:
    
    even = sum(1 for num in nums if num % 2 == 0)
    odd = len(nums) - even
    return f"Result: Even: {even}, Odd: {odd}"

print(even_and_odd([1, 2, 3, 4, 5]))