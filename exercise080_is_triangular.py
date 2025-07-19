# Napisz funkcję, która sprawdza, czy dana liczba jest liczbą trójkątną 
# (czy można ją przedstawić jako 1 + 2 + ... + k dla jakiegoś k).
# Przykład wywołania: is_triangular(10) Wynik: True (10 = 1+2+3+4)
# n = (−1 + √(1 + 8x)) / 2
def is_triangular(num: int) -> bool:
    return ((-1 + (1 + (8* num))**0.5) / 2).is_integer()

print(is_triangular(10))