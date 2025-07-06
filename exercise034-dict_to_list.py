# Napisz funkcję dict_to_list(), która przyjmuje słownik i zwraca listę krotek (key, value).

def dict_to_list(dictionary: dict) -> list:
    keys = []
    for key in dictionary:
        keys.append((key, dictionary[key]))
    return keys

print(dict_to_list({"a": 1, "b": 2, "c": 3}))