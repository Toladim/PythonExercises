# Napisz funkcję, która zastępuje wszystkie spacje w łańcuchu znakiem podkreślenia _.
# Przykład wywołania: underscore("to be or not to be") Wynik: "to_be_or_not_to_be"
def underscore(text: str) -> str:
    return text.replace(" ", "_")

print(underscore("to be or not to be"))