""" Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""

def generate_fibonacci(n):
    if n < 0:
        return[]
    elif n == 0:
        return [1]
    elif n == 1:
        return [1,1]
    else:
        fib = [1,1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib

try:
    num = int(input("Enter the number of Fibonacci numbers to generate: "))
    if num > 0:
        print(f"The first {num} Fibonacci numbers are: {generate_fibonacci(num)}")
except ValueError:
    print("Invalid input. Please enter an integer.")