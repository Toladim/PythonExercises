# Napisz funkcję, która oblicza sumę pierwszych N wyrazów zadanej progresji arytmetycznej 
# (progresja określona przez pierwszy wyraz a1 i różnicę d).
# Przykład wywołania: ap_sum(3, 2, 5) Wynik: 35 (dla a1=3, d=2 sumujemy: 3+5+7+9+11)
# Sₙ = n × [2a₁ + (n − 1) × r] / 2

def ap_sum(start_num: int, diff: int, scope: int) -> int:
    total = [start_num]
    last_num = start_num
    for _ in range(1, scope):
        last_num += diff
        total.append(last_num)
    return sum(total)

print(ap_sum(3, 2, 5))

# def ap_sum(a1: int, d: int, n: int) -> int:
#     return n * (2 * a1 + (n - 1) * d) // 2
