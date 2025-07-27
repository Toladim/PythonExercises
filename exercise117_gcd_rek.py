# Napisz funkcję rekurencyjną, która oblicza NWD (największy wspólny dzielnik) dwóch liczb.
# Przykład wywołania: gcd_rek(48, 18) Wynik: 6
def gcd_rek(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return gcd_rek(num2, num1 % num2)

print(gcd_rek(48, 18))