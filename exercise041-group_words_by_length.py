# Napisz funkcję, która przyjmie listę słów i zwróci słownik, 
# w którym kluczami będą długości słów, a wartościami — listy słów o danej długości.

def group_words_by_length(words: list[str]) -> dict[int, list[str]]:
    words_by_length = {}
    for word in words:
        length = len(word)
        words_by_length.setdefault(length, []).append(word)
    return words_by_length

print(group_words_by_length(["hi", "hello", "cat", "python", "to"]))