# Napisz funkcję, która przyjmie listę słów i zwróci je posortowane rosnąco według długości.
# Nie używaj .sort() w miejscu — zwróć nową listę.

def sort_words(sentence: list[str]) -> list[str]:
    return sorted(sentence, key=len)

print(sort_words(["Hello","wORlD", "python", "USA"]))