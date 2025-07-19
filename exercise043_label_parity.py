# Napisz funkcję, która przyjmie listę liczb całkowitych i zwróci nową listę, 
# w której każda liczba zostanie zastąpiona słowem - "even" jeśli parzysta, "odd" jeśli nieparzysta
def label_parity(nums: list[int]) -> list[str]:
    return ["even" if num % 2 == 0 else "odd" for num in nums]

print(label_parity([1, 2, 3, 4, 5]))

