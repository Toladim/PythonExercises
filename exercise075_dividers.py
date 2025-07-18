# Napisz funkcję, która zwraca listę wszystkich dzielników danej liczby.
# Przykład wywołania: dyvider(12) Wynik: [1, 2, 3, 4, 6, 12]
def dividers(num: int) -> list[int]:
    divs = set()
    for n in range(1, int(num ** 0.5) + 1):
         if num % n == 0:
              divs.add(n)
              divs.add(num//n)
    return sorted(divs)

print(dividers(12))
