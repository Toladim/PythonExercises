# Napisz funkcję rekurencyjną, która odwraca łańcuch znaków.
# Przykład wywołania: reverse_rec("abcd") Wynik: "dcba"
def reverse_rec(text: str) -> str:
    if text == "":
        return ""
    else:
        print(text)
        return reverse_rec(text[1:]) + text[0]
    
print(reverse_rec("abcd"))