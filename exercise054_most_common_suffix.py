# Napisz funkcję, która:
# przyjmie taki słownik,
# zwróci końcówkę (czyli klucz), która ma najwięcej słów w liście.

def most_common_suffix(words_dict: dict[str, list[str]]) -> str:
    return max(words_dict, key=lambda suffix: len(words_dict[suffix]))

print(most_common_suffix({
    "ng": ["king", "ring", "thing", "fling"],
    "at": ["cat", "hat", "bat"]
}))


