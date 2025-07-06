# Napisz funkcję replace_vowels(), która przyjmie łańcuch znaków (string) i zwróci nowy string, 
# w którym wszystkie samogłoski zostaną zastąpione gwiazdką (*).
def replace_vowels(text: str) -> str:
    vowels = ["a","e","i","o","u","y"]
    new_text = ""
    for char in text:
        if char.lower() in vowels:
            new_text += "*"
        else:
            new_text += char
    return new_text

print(replace_vowels("hello world"))