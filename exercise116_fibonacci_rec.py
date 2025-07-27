# Napisz funkcję rekurencyjną, która zwraca n-ty wyraz ciągu Fibonacciego.
# Przykład wywołania: fibonacci(6) Wynik: 8 (6-ty wyraz to 8, przy założeniu fib(1)=1, fib(2)=1)
def fibonacci_rec(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    
print(fibonacci_rec(6))



