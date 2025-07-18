# Napisz funkcję, która sprawdza, czy dana liczba należy do ciągu Fibonacciego 
# (np. poprzez wygenerowanie ciągu do momentu przekroczenia tej liczby).
# Przykład wywołania: belongs_to_fib(8) Wynik: True (8 jest elementem ciągu Fibonacciego)
def belongs_to_fib(num: int) -> bool:
    a, b = 1, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False

print(belongs_to_fib(8))