# Napisz funkcję, która przyjmie listę liczb i zwróci nową listę zawierającą tylko liczby pierwsze.
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

def filter_primes(nums: list[int]) -> list[int]:
    primes_nums = []
    for n in nums:
        if is_prime(n):
            primes_nums.append(n)
    return primes_nums

print(filter_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]))