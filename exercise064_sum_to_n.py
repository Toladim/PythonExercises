# Napisz funkcję, która oblicza sumę wszystkich liczb naturalnych od 1 do N.
# Przykład wywołania: sum_to_n(5) Wynik: 15 

def sum_to_n(max_num: int) -> int:
    return sum([num for num in range(1, max_num + 1)])

print(sum_to_n(5))
