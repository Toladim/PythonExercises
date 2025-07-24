# Napisz funkcję, która odwraca podany łańcuch znaków.
# Przykład wywołania: revers_string("ABC") Wynik: "CBA"
def reverse_string(text: str) -> str:
    return text[::-1]

print(reverse_string("ABC"))
