# Napisz funkcję rekurencyjną, która sprawdza, czy łańcuch jest palindromem.
# Przykład wywołania: palindrom_rec("kajak") Wynik: True
def palindrom_rec(text: str) -> bool:
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    
    return palindrom_rec(text[1:-1])
    
print(palindrom_rec("kajak"))