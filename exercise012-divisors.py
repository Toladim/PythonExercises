"""/Create a program that asks the user for a number 
and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""

def find_divisors(num):
    return [i for i in range(1, num+1) if num % i == 0]
    
    """temp = []
    for i in range (1, num+1):
        if num % i == 0:
            temp.append(i)
    return temp"""
            
user_input = int(input("Type some number: "))

print(find_divisors(user_input))