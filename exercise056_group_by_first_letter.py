# Napisz funkcję, która:
# przyjmie listę słów (mogą być z dużych i małych liter),
# pogrupuje je według pierwszej litery (litery małe),
# zwróci słownik: klucz = pierwsza litera, wartość = lista słów zaczynających się od niej
def group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    grouped_words = {}
    for word in words:
        if word[0].lower() not in grouped_words:
            grouped_words[word[0].lower()] = []
        grouped_words[word[0].lower()].append(word)
    return grouped_words

group_by_first_letter(["Apple", "ant", "Ball", "banana", "cat", "Car"])