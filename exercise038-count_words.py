# Napisz funkcję count_words(text: str) -> int, która zwróci liczbę słów w zdaniu.
# Słowa są oddzielone spacjami (ignoruj przecinki, kropki itp. na razie).

def count_words(text: str) -> int:
    words = text.strip().split()
    return len(words)
    
print(count_words("Hello world this is Python"))
