# Napisz funkcję, która rotuje listę o k pozycji w lewo 
# (tzn. przenosi pierwsze k elementów na koniec listy).
# Przykład wywołania: rotate_list([1, 2, 3, 4, 5], 2) Wynik: [3, 4, 5, 1, 2]
def rotate_list(items: list[int], how_far: int) -> list[int]:
   how_far = how_far % len(items)
   return items[how_far:] + items[:how_far]

print(rotate_list([1, 2, 3, 4, 3, 3, 3, 4, 5], 100))