# Napisz funkcję, która zwraca najdłuższe słowo w zdaniu.
# Przykład wywołania: longest_word("Ala ma kota") Wynik: "kota"
def longest_word(text: str) -> str:
    return max(text.split(), key=len)
        
print(longest_word("Ala ma kota"))