# Napisz funkcję, która oblicza wartość symbolu Newtona C(n, k) 
# (tzw. n choose k = C(n, k)), wykorzystując funkcję silnia(n) z poprzedniej fazy.
# Przykład wywołania: n_choose_k(5, 2) Wynik: 10 (ponieważ 5 choose 2 = 10)
# C(n, k) = n! / (k! × (n − k)!)
from exercise066_factorial_sum import factorial

def n_choose_k(n: int, k: int) -> int:
    return (factorial(n) // (factorial(k) * factorial(n - k)))

print(n_choose_k(5, 2))