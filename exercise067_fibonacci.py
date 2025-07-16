# Napisz funkcję, która generuje pierwsze N liczb Fibonacciego.
# Przykład wywołania: fibonacci(6) Wynik: [1, 1, 2, 3, 5, 8]

def fibonacci(n):
    a, b = 1, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

print(fibonacci(6))