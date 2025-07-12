# Napisz funkcję, która przyjmie dwa stringi i sprawdzi, czy są anagramami — 
# czyli mają dokładnie te same litery w różnych kolejnościach 
# (ignorując wielkość liter, pomijając znaki niealfabetyczne).
def are_anagrams(text_1: str, text_2: str) -> bool:
    letters_from_text_1 = {}
    letters_from_text_2 = {}
    letters_from_text_1 = letter_to_dict(text_1)
    letters_from_text_2 = letter_to_dict(text_2)
    return letters_from_text_1 == letters_from_text_2

def letter_to_dict(text: str) -> dict[str, int]:
    letters_from_text = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letters_from_text[char] = letters_from_text.get(char, 0) + 1
    return letters_from_text


print(are_anagrams("Listen", "Silent"))
print(are_anagrams("Hello", "World")) 