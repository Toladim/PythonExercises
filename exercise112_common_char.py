# Napisz funkcję, która znajduje najczęściej występujący znak w łańcuchu.
# Przykład wywołania: common_char("abbccc") Wynik: "c"
def common_char(text: str) -> str:
    most = {}
    for char in text:
        most[char] = most.get(char, 0) + 1
    return max(most, key=most.get)

print(common_char("abbccc"))