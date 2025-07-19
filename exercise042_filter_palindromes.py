# Napisz funkcję, która przyjmie listę stringów i zwróci nową listę zawierającą tylko te stringi, 
# które są palindromami (czyli czytane od tyłu wyglądają tak samo).
def filter_palindromes(text_list: list[str]) -> list[str]:             
    return [text for text in text_list if text == text[::-1]]

print(filter_palindromes(["kayak", "hello", "level", "world", "madam"]))