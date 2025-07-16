# Napisz funkcję, która sprawdza, czy dana liczba jest liczbą Armstronga (np. 153 = 1^3 + 5^3 + 3^3).
# Przykład wywołania: is_armstrong(153) Wynik: True
def is_armstrong(num: int) -> bool:
    power = len(str(num))
    return num == sum(int(digit) ** power for digit in str(num))

print(is_armstrong(54748))