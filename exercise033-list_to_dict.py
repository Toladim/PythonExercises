# Napisz funkcję list_to_dict(), która przyjmuje listę krotek (ang. tuples) 
# zawierających pary klucz–wartość i zwraca słownik (dict) z tych par.

def list_to_dict(items: list) -> dict:
    return dict(items)

print(list_to_dict([("a", 1), ("b", 2), ("c", 3)]))