# Napisz funkcję, która sprawdza, czy dana liczba jest palindromem 
# (tzn. czy czyta się tak samo od przodu i od tyłu).
# Przykład wywołania: is_palindrom_num(121) Wynik: True

def is_palindrom_num(num: int) -> bool:
    return str(num) == str(num)[::-1]

print(is_palindrom_num(1321))