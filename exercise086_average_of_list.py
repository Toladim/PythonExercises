# Napisz funkcję, która oblicza średnią arytmetyczną listy liczb 
# (wykorzystaj funkcję sumy z poprzedniego zadania).
# Przykład wywołania: average_of_list([2, 4, 6]) Wynik: 4.0
from exercise085_sum_of_list import sum_of_list

def average_of_list(nums: list[int]) -> float:
    return (sum_of_list(nums) / len(nums))

print(average_of_list([2, 4, 6]))