""" 
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:
1.Randomly generate two lists to test this
2.Write this in one line of Python 
(don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

min_elements, max_elements = 5, 15
min_value, max_value = 1, 24

"""for i in range(random.randint(min_threshold_elements, max_threshold_elements+1)):
    list_1.append(random.randint(min_threshold_value, max_threshold_value))

for i in range(random.randint(min_threshold_elements, max_threshold_elements+1)):
    list_2.append(random.randint(min_threshold_value, max_threshold_value))"""

def create_random_list(min_range, max_range, min_value, max_value):
    return [random.randint(min_value, max_value+1)
    for _ in range(random.randint(min_range, max_range+1))]

def show_commons(list_a, list_b):
    return list(set([i for i in list_a for j in list_b if i==j]))


random_list_1 = create_random_list(min_elements, max_elements, min_value, max_value)
random_list_2 = create_random_list(min_elements, max_elements, min_value, max_value)

print(show_commons(a, b))
print(f"""First list: {random_list_1}
Second list: {random_list_2}
Common elements: {show_commons(random_list_1, random_list_2)}.""")
