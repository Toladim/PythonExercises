# Napisz funkcję, która sprawdza, czy dwa łańcuchy są anagramami 
# (czy z liter jednego można ułożyć drugi).
# Przykład wywołania: are_anagrams("tokio", "kioto") Wynik: True

def are_anagrams(text1: str, text2: str) -> bool:
    return sorted(text1.lower()) == sorted(text2.lower())

print(are_anagrams("tokio", "kioto"))