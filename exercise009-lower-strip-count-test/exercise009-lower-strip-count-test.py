"""/Napisz program, który liczy, ile razy określone słowo występuje w danym tekście.

1.Poproś użytkownika o wprowadzenie długiego tekstu.
2.Następnie zapytaj, jakie słowo chce wyszukać.
3.Program powinien ignorować wielkość liter i spacje na początku i końcu tekstu lub wyszukiwanego słowa."""

long_text = input("Type some long text: ")
searched_text = input ("Type word to search: ")

def normalize_string(text):
    text = text.lower()
    text = text.strip()
    return text

normalized_long_text = normalize_string(long_text)
normalized_search = normalize_string(searched_text)

print(f"Word {normalized_search}, occurs in text {normalized_long_text.count(normalized_search)} times.")