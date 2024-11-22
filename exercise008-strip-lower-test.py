"""\Porównywanie tekstów z różnym formatowaniem"""
#Napisz program, który porównuje dwa wprowadzone przez użytkownika ciągi znaków (np. imiona) 
# i sprawdza, czy są takie same, ignorując wielkość liter
#oraz ewentualne dodatkowe spacje na początku i końcu.

def normalize_string(text):
    text = text.strip()
    text = text.lower()
    return text

input_text_1 = input("Type first word to compare: ")
input_text_2 = input("Type first word to compare: ")

normalized_text_01 = normalize_string(input_text_1)
normalized_text_02 = normalize_string(input_text_2)

if normalized_text_01 == normalized_text_02:
    print("Words are identical.")
else:
    print("Words are not identical.")