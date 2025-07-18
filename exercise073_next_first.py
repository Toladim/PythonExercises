# Napisz funkcję, która znajduje najmniejszą liczbę pierwszą większą od danej liczby N 
# (wykorzystaj funkcję sprawdzającą pierwszość z poprzedniej fazy).
# Przykład wywołania: next_first(10) Wynik: 11

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_first(num: int) -> int:
    num += 1
    while not is_prime(num):
        num += 1
    return num

print(next_first(10))