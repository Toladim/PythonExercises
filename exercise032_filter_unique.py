# Napisz funkcję filter_unique(), 
# która przyjmie listę liczb całkowitych i zwróci nową listę zawierającą tylko te liczby, 
# które występują dokładnie raz.

def filter_unique(numbers: list[int]) -> list[int]:
    filtered_list = []
    for n in numbers:
        if numbers.count(n) == 1:
            filtered_list.append(n)
    return(filtered_list)

print(filter_unique([1, 2, 2, 3, 3, 3, 4]))