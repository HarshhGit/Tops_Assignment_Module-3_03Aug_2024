# Q.43]  Write a Python function to calculate the factorial of a number (a nonnegative integer)

import math


def fact(n):
    if n < 0:
        raise ValueError("Given number is invalid")
    return math.factorial(n)
    

user = int(input("Enter number to get factorial: "))
print("Factorial of given number is: ",fact(user))