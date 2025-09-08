# Napisz funkcję, która zlicza liczbę cyfr w zadanej liczbie (rekurencyjnie).
# Przykład wywołania: count_digits_rec(5020) Wynik: 4

def count_digits_rec(num: int) -> int:
    if num < 10:
        return 1
    else:
        return count_digits_rec(num // 10) + 1
    
print(count_digits_rec(5020))