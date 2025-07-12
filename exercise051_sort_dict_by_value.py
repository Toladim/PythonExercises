# Napisz funkcję, która przyjmie słownik, gdzie:
# klucz to słowo (str),
# wartość to liczba (int),
# ...i zwróci listę krotek (słowo, liczba) posortowaną malejąco po liczbach.
def sort_dict_by_value(dictionary: dict[str, int]) -> list[tuple[str, int]]:
    dictionary.pair
    return sorted(dictionary.items(), key=lambda pair: pair[1], reverse=True)

print(sort_dict_by_value({"apple": 5, "banana": 2, "cherry": 8}))