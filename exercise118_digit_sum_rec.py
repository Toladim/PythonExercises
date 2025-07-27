# Napisz funkcję rekurencyjną, która oblicza sumę cyfr danej liczby.
# Przykład wywołania: digit_sum_rec(123) Wynik: 6
def digit_sum_rec(num: int) -> int:
    if num == 0:
        return 0
    else:
        return (num % 10) + digit_sum_rec(num // 10)

print(digit_sum_rec(123))