# Napisz funkcję, która sprawdza, czy dana liczba jest liczbą szczęśliwą (happy number).
# Przykład wywołania: is_happy_number(19) Wynik: True
def is_happy_number(num: int) -> bool:
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(d)**2 for d in str(num))
    return num == 1

print(is_happy_number(19))