# Napisz funkcję count_unique_characters(text: str) -> int, 
# która przyjmie łańcuch znaków i zwróci liczbę różnych (unikalnych) znaków w tym stringu.

def count_unique_characters(text: str) -> int:
    unique_chars = ""
    unique_total = 0
    for char in text:
        if char.lower() not in unique_chars:
            unique_chars += char
            unique_total += 1
    return unique_total

print(count_unique_characters("hello world"))
        