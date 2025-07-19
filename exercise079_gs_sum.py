# Napisz funkcję, która oblicza sumę pierwszych N wyrazów ciągu geometrycznego 
# (określonego przez pierwszy wyraz a1 i iloraz q).
# Przykład wywołania: gs_sum(2, 3, 4) Wynik: 80 (dla a1=2, q=3 sumujemy: 2 + 6 + 18 + 54 = 80)
# Sₙ = a₁ × (qⁿ − 1) / (q − 1)

def gs_sum(a1: int, q: int, n: int) -> int:
    return a1 * ((q ** n) - 1) // (q - 1)

print(gs_sum(2, 3, 4))

