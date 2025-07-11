# Napisz funkcję, która:
# przyjmie listę słów,
# pogrupuje je według końcówki (word[-2:]),
# zwróci słownik: klucz to końcówka, wartość to lista słów z taką końcówką

def group_by_suffix(words: list[str]) -> dict[str, list[str]]:
    suffix_groups = {}
   
    for word in words:
        if word[-2:] not in suffix_groups:
            suffix_groups[word[-2:]] = []
        suffix_groups[word[-2:]].append(word)

    return suffix_groups
        
    
        
print(group_by_suffix(["king", "ring", "cat", "hat", "thing", "bat", "fling"]))