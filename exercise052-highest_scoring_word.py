# Napisz funkcję, która przyjmie listę słów i zwróci to, które ma największy łączny wynik Scrabble.
points = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2,
    'e': 1, 'f': 4, 'g': 2, 'h': 4,
    'i': 1, 'j': 8, 'k': 5, 'l': 1,
    'm': 3, 'n': 1, 'o': 1, 'p': 3,
    'q': 10,'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10
}

def highest_scoring_word(words: list[str]) -> str:
    words_points = {}
    for word in words:
        for letter in word:
            words_points[word] = words_points.get(word, 0) + points[letter]
    return max(words_points, key=words_points.get)

print(highest_scoring_word(["hello", "quiz", "banana", "zap"]))