# Napisz funkcję, która przyjmie tekst i zwróci literę, która występuje najczęściej 
# (ignorując wielkość liter i pomijając znaki niebędące literami).
def most_common_letter(text: str) -> str:
    letters_common = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letters_common[char] = letters_common.get(char, 0) + 1
    return max(letters_common,key=letters_common.get)
    

print(most_common_letter("Hello, world!"))
