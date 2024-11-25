""" Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)"""

user_string = input("Type some string to prove that is palindrome or not: ")

def is_palindrome(string):
    normalized_string = "".join(string.lower().strip())
    return normalized_string == normalized_string[::-1]

if is_palindrome(user_string):
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")

