# Zmodyfikuj funkcję z exc056 (lub napisz nową), która:
# bierze słownik taki jak zwraca group_by_first_letter(...),
# sortuje listę słów w każdej grupie alfabetycznie, ignorując wielkość liter,
# zwraca nowy słownik z tymi posortowanymi listami.
from exercise056_group_by_first_letter import group_by_first_letter

def sort_groups(words_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    return {}


groups = group_by_first_letter(["Apple","Olgiert", "Car", "ant", "Ball", "banana", "cat"])
print(sort_groups(groups))