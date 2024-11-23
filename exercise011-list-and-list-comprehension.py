"""/
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1.Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.
2.Write this in one line of Python.
3.Ask the user for a number and return a list that contains only 
elements from the original list a that are smaller than that number given by the user."""



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def filter_list(input_list, threshold):
  return [element for element in input_list if element <= threshold]

try:
  user_input = int(input("Enter a threshold number " \
  "(elements less than or equal to this number will be selected): "))
  result = filter_list(a, user_input)
  print(f"Elements in the list less than or equal to {user_input}: {result}")
except ValueError:
  print("Invalid input. Please enter a valid integer!")

# One-liner version (optional)
# print([x for x in a if x <= int(input("Enter a threshold number: "))])