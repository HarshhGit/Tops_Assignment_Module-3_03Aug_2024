# Q.48]   Write a Python program to convert degree to radian

import math

def degree_radians(d):
    return math.radians(d)

user = float(input("Enter angle in degrees: "))
radians = degree_radians(user)

print(f"{user} degrees is {radians} radians.")