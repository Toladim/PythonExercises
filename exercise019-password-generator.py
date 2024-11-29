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

def generate_password(difficulty):
    if difficulty == "easy":
        length = random.randint(5,9)
        sequence = (string.ascii_lowercase) * 3 + string.ascii_uppercase + string.digits
    elif difficulty == "medium":
        length = random.randint(8,12)
        sequence = (string.ascii_lowercase) * 3 + (string.ascii_uppercase) * 2 + string.digits + string.punctuation
    elif difficulty == "hard":
        length = random.randint(11,15)
        sequence = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        raise ValueError("Invalid difficulty level")

    return "".join(random.choice(sequence) for _ in range(length))

def main():
    valid_difficulties = ["easy", "medium", "hard"]
    while True:
        password_difficulty = input("Type how difficult password should be (easy/medium/hard): ").lower()
        if password_difficulty in valid_difficulties:
            password = generate_password(password_difficulty)
            print(f"That's your {password_difficulty} password: {password}")
            break
        else:
            print(f"Invalid input. Please choose one of the following: {', '.join(valid_difficulties)}.")


if __name__ == "__main__":
    main()

