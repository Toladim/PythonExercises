# Napisz funkcję, która kompresuje łańcuch znaków wg run-length encoding (np. "aaabbc" -> "a3b2c1").
# Przykład wywołania: encode_string("aaabbc") Wynik: "a3b2c1"
def encode_string(text: str) -> str:
    if not text:
        return ""
    encoded = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded += text[i - 1] + str(count)
            count = 1
    encoded += text[-1] + str(count)

    return encoded

print(encode_string("aaabbc"))