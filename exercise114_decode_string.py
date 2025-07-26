# Napisz funkcję, która dekompresuje łańcuch w formacie run-length encoding (np. "a3b2c1" -> "aaabbc").
# Przykład wywołania: decode_string("a3b2c1") Wynik: "aaabbc"
def decode_string(text: str) -> str:
    decoded_text = ""
    i = 0
    while i < len(text):
        char = text[i]
        i += 1
        num_str = ""
        while i < len(text) and text[i].isdigit():
            num_str += text[i]
            i += 1
        decoded_text += char * int(num_str)
    return decoded_text

print(decode_string("a3b2c1"))