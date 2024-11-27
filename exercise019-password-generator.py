"""Note: this is a 4-chili exercise, not because it introduces a concept,
but because this exercise is more like a project.
Feel free to skip this and come back when you’re more ready!

Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list."""
import random
import string

def generate_password(lenght, difficult):

    sequence = (string.ascii_lowercase) * 2 + (string.ascii_uppercase) * 2 + string.digits + string.punctuation
    return "".join(random.choice(sequence) for _ in range(lenght))
while True:
    input_difficult = ("Type how difficult password could be(easy/medium/hard): ")
    #if input_difficult == 

print(generate_password(15))