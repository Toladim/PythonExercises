# Napisz funkcję rekurencyjną, która oblicza silnię liczby n.
# Przykład wywołania: factorial(5) Wynik: 120
def factorial_rec(num: int) -> int:
    if num < 0:
        print("Error")
    if num == 0  or num == 1:
        return 1
    return num * factorial_rec(num - 1)

print(factorial_rec(5))