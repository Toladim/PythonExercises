# Napisz funkcję, która rozwiązuje problem Wież Hanoi dla n krążków 
# (zwraca listę ruchów potrzebnych do przeniesienia wszystkich krążków).
# Przykład wywołania: hanoi(2) Wynik: ["A->B", "A->C", "B->C"] (kolejne ruchy dla 2 krążków)
def hanoi(n: int) -> list[str]:
    def move_disk(n: int, source: str, helper: str, target: str, moves: list[str]):
        if n == 1:
            moves.append(f"{source}->{target}")
        else:
            move_disk(n - 1, source, target, helper, moves)
            moves.append(f"{source}->{target}")
            move_disk(n - 1, helper, source, target, moves)

    result = []
    move_disk(n, "A", "B", "C", result)
    return result
    
print(hanoi(6))