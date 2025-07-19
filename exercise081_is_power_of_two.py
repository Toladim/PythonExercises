# Napisz funkcję, która sprawdza, czy dana liczba jest potęgą dwójki.
# Przykład wywołania: is_power_two(16) Wynik: True
def is_power_of_two(num: int) -> bool:
    return num & (num - 1)

print(is_power_of_two(16))