# Napisz funkcję, która sprawdza, czy dany łańcuch znaków jest palindromem (ignorując wielkość liter).
# Przykład wywołania: is_palindrom("Kajak") Wynik: True 
# (po zignorowaniu wielkości liter "Kajak" to palindrom)
def is_palindrom(text: str) -> bool:
    text = text.lower()
    return text == text[::-1]

print(is_palindrom("Kajak"))