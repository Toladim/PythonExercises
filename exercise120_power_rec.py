# Napisz funkcję rekurencyjną, która podnosi liczbę a do potęgi b.
# Przykład wywołania: power_rec(2, 5) Wynik: 32
def power_rec(num1: int, num2: int) -> int:
    if num2 == 0:
        return 1
    else:
        return power_rec(num1, num2 - 1) * num1
    
print(power_rec(2, 5))