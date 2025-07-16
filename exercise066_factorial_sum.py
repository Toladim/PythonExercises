# Napisz funkcję, która oblicza sumę ciągu silni od 1! do N!
# Przykład wywołania: factorial_sum(4) Wynik: 33 (ponieważ 1!+2!+3!+4! = 33)
def factorial_sum(num: int) -> int:
    return sum(factorial(n) for n in range(1, num + 1))

def factorial(num: int) -> int:
    return 1 if num == 0 else num * factorial(num - 1)

print(factorial_sum(4))