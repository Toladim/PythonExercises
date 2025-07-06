# Napisz funkcję, która przyjmie tekst i zwróci listę słów, które mają więcej niż 4 litery.
def filter_long_words(text: str)-> list:
    words = text.split()
    words_list = []
    for word in words:
        if len(word) > 4:
            words_list.append(word)    
    return words_list


print(filter_long_words("The quick brown fox jumps over the lazy dog"))