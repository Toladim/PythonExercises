# Napisz funkcję rekurencyjną, która wypisuje liczby od 1 do N (lub zwraca je w liście).
# Przykład wywołania: print_rec(5) Wynik: [1, 2, 3, 4, 5]
def print_rec(num: int) -> list[int]:
    if num == 0:
        return []
    return print_rec(num - 1) + [num]
    
print(print_rec(5))
