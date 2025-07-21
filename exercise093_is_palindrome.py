# Napisz funkcję, która sprawdza, czy lista jest palindromem 
# (czyli czy czyta się tak samo od początku do końca i od końca do początku).
# Przykład wywołania: is_palindrome([1, 2, 3, 2, 1]) Wynik: True
def is_palindrome(nums: list[int]) -> bool:
    return (nums == nums[::-1])

print(is_palindrome([1, 2, 3, 2, 1]))