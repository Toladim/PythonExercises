# Napisz funkcję, która oblicza sumę cyfr danej liczby.
# Przykład wywołania: digit_sum(1234) Wynik: 10 (1+2+3+4)
def digit_sum(num: int) -> int:
    return sum(int(n) for n in str(num))

print(digit_sum(1234))