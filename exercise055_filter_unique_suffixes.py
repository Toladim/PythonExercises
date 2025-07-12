# Napisz funkcję, która przyjmie słownik (tak jak wcześniej — końcówka → lista słów),
# i zwróci nowy słownik, zawierający tylko te końcówki, które mają dokładnie jedno słowo.
def filter_unique_suffixes(words_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    return {suffix: words for suffix, words in words_dict.items() if len(words) == 1}

print(filter_unique_suffixes({
    "ng": ["king", "ring"],
    "at": ["cat", "hat", "bat"],
    "ow": ["cow"],
    "ed": ["bed", "red"],
    "ix": ["phoenix"]
}))