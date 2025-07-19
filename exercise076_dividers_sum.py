# Napisz funkcję, która oblicza sumę wszystkich dzielników właściwych danej liczby 
# (możesz wykorzystać funkcję z zadania 75).
# Przykład wywołania: dividers_sum(12) Wynik: 16 (1+2+3+4+6 = 16)
from exercise075_dividers import dividers

def dividers_sum(num: int) -> int:
    return sum(d for d in dividers(num))- num
        
print(dividers_sum(12))