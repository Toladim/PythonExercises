# Napisz funkcję, która oblicza liczbę zer na końcu wyniku silni N! 
# (tzn. ile zer występuje na końcu liczby N!).
# Przykład wywołania: factorial_zeros(10) Wynik: 2 (10! = 3 628 800, końcowe zera: 2)
from exercise066_factorial_sum import factorial

def factorial_zeros(num: int) -> int:
    zeros = 0
    for n in str(factorial(num))[::-1]:
        if n == "0":
            zeros += 1
        else:
            return zeros

print(factorial_zeros(10))

# def factorial_zeros(num: int) -> int:
#     count = 0
#     while num >= 5:
#         num //= 5
#         count += num
#     return count
