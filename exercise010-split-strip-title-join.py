"""/Formatowanie listy imion
Napisz program, który przyjmuje od użytkownika listę imion (wpisanych w jednej linii,
rozdzielonych przecinkami), a następnie zwraca je w formacie:

1.Wszystkie imiona z wielką literą na początku (np. "anna" → "Anna").
2.Posortowane alfabetycznie.
3.Połączone w jeden ciąg, rozdzielone przecinkami i spacją."""


input_text = input("Type list of names (entered in a single line, separated by commas): ")

def normalize_string(text):
    text = text.title()
    text = text.split(",")
    text = [item.strip() for item in text]
    sorted_text = ", ".join(sorted(text))
    return sorted_text

print(normalize_string(input_text))
