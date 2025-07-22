# Napisz funkcję, która usuwa z listy elementy powtarzające się 
# (pozostawiając tylko unikalne wartości).
# Przykład wywołania: unique([1, 2, 2, 3, 3, 3]) Wynik: [1, 2, 3]
def unique(items: list[int]) -> list[int]:
    return list(set(items))

print(unique([1, 2, 2, 3, 3, 3]))