# # Napisz funkcję, która generuje ciąg Collatza (3n+1) dla zadanej liczby startowej, aż do osiągnięcia 1.
# # Przykład wywołania: collatz(6) Wynik: [6, 3, 10, 5, 16, 8, 4, 2, 1]
# Jeśli liczba jest parzysta – dzielisz ją przez 2.
# Jeśli liczba jest nieparzysta – mnożysz ją przez 3 i dodajesz 1

def collatz(num: int) -> list[int]:
    if num == 1:
        return [1]
    if num % 2 == 0:
        next_num = num // 2
    else:
        next_num = num * 3 + 1   
    return [num] + collatz(next_num)
        
print(collatz(6))