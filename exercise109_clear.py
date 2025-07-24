# Napisz funkcję, która usuwa z łańcucha wszystkie znaki niebędące literami ani cyframi 
# (czyli pozostawia tylko litery i cyfry).
# Przykład wywołania: clear("Hello, World! 123") Wynik: "HelloWorld123"

def clear(text: str) -> str:
    return "".join (char for char in text if char.isalnum())

print(clear("Hello, World! 123"))