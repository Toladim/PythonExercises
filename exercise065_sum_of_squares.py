# Napisz funkcję, która oblicza sumę kwadratów liczb od 1 do N.
# Przykład wywołania: sum_of_squares(3) Wynik: 14 (ponieważ 1^2 + 2^2 + 3^2 = 14)
def sum_of_squares(num: int) -> int:
    return sum(n**2 for n in range(1, num + 1))

print(sum_of_squares(3))