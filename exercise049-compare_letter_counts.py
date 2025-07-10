# Napisz funkcję, która przyjmie dwa teksty i zwróci słownik pokazujący, ile razy więcej (lub mniej) 
# każda litera występuje w pierwszym tekście względem drugiego.
def compare_letter_counts(text_1: str, text_2: str) -> dict[str, int]:
    letters_from_text_1 = letter_to_dict(text_1)
    letters_from_text_2 = letter_to_dict(text_2)
    compared_letters = {}
    
    all_keys = set(letters_from_text_1) | set(letters_from_text_2)

    for key in all_keys:
        count_1 = letters_from_text_1.get(key, 0)
        count_2 = letters_from_text_2.get(key, 0)
        compared_letters[key] = count_1 - count_2

    return compared_letters

def letter_to_dict(text: str) -> dict[str, int]:
    letters_from_text = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letters_from_text[char] = letters_from_text.get(char, 0) + 1
    return letters_from_text

print(compare_letter_counts("hello", "hola"))