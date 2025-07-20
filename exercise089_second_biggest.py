# Napisz funkcję, która znajduje drugą największą liczbę w liście.
# Przykład wywołania: second_biggest([4, 7, 2, 9, 5]) Wynik: 7

def second_biggest(nums: list[int]) -> int:
    unique = sorted(set(nums), reverse=True)
    return unique[1] if len(unique) > 1 else None

print(second_biggest([4, 7, 2, 9, 5]))