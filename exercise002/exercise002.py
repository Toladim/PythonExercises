number = int(input("Give some number: "))

if number % 4 == 0:
    print(f"{number} print out a different message.")
elif number % 2 == 0:
    print(f"{number} is odd")
else:
    print(f"{number} is even")