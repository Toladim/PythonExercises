"""Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. 
For example, say I type the string:
    My name is Michele
Then I would see the string:
    Michele is name My
shown back to me."""

def backward_string(some_string):
    some_string = some_string.split()
    some_string = some_string[::-1]
    return " ".join(some_string)

print(backward_string("My name is Michele"))