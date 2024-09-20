""" Q.41}  Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300}) """

from collections import Counter

#sample data with items and amount
sample_data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

combined_count = Counter()#this empty counter will hold combined values

for value in sample_data:
    combined_count[value['item']] += value['amount']

print("Combined values in dictionary: ", combined_count)


""" Q.42}  Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}"""

sample_string = 'w3resource'
#empty dictionary will hold the counted character 
char_count = {}

for char in sample_string:
#it will check if char isin char_count if exist more than 1 it will increse by 1 else assign as 1
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Total char in given string: ", char_count) 


# Q.43]  Write a Python function to calculate the factorial of a number (a nonnegative integer)

import math


def fact(n):
    #it will give error if input is less than 0
    if n < 0:
        raise ValueError("Given number is invalid")
    return math.factorial(n)
    
#gets user input to find the factorial
user = int(input("Enter number to get factorial: "))
print("Factorial of given number is: ",fact(user))

# Q.44]  Write a Python function to check whether a number is in a given range
#this will check if a number is in range or not
def in_range(num,start,end):
    return start <= num <= end

print(in_range(5,0,15)) #True
print(in_range(15,20,10)) #False bcz number is 15 and range starting from 20
print(in_range(24,1,25)) #True
print(in_range(3,10,15)) #False
print(in_range(15,1,30)) #True


# Q.45]Write a Python function to check whether a number is perfect or not.


def perfect(n):
    sum = 0
    #loop from 1 to n-1 
    for i in range(1,n):
        if n%i == 0:
            sum = sum + i
#if sum is equal to the number after loop it is perfect else its not
    if sum == n:
        return (f"Yes {n} is a perfect number")
    else:
        return(f"{n} isn't a perfect number")

user = int(input("Enter a number to check perfect or not: "))

print(perfect(user))

# Q.46]  Write a Python function that checks whether a passed string is palindrome or not 


#check if a number palindrome or not (a string number that reads same as backword)
def palindrome(s):
    normal_str = s.replace(" ","").lower()
#using lower it will normalise the input and using replace it will remove extra or given space
    return normal_str == normal_str[::-1]
#it will give reverse string using negative indexing.
user = input("Enter a string to check its palindrome or not: ")
print("Given string is palindrome : ",palindrome(user))


# Q.47]  Write a Python program to read a random line from a file.

import random
#fun to read a random line from file using 'r' method which is for read and readlines() that reades lines from file 
def read_file(file_path):
    f = open(file_path,'r')
    lines = f.readlines()
    f.close()

    if lines:
    #using random.choice() will pick random line from lines and using strip() it will will remove extra whitespace from line
        random_line = random.choice(lines)
        return random_line.strip()
    
file_path = 'Th.txt'
print(read_file(file_path))


# Q.48]   Write a Python program to convert degree to radian
#function to convert degrees to radians using math.radians() module
def degree_radians(d):
    return math.radians(d)

user = float(input("Enter angle in degrees: "))
radians = degree_radians(user)

print(f"{user} degrees is {radians} radians.")

# Q.49]  Write a Python program to calculate the area of a trapezoid
#this will calculate area of a trapezoid
def trapezoid_area(b1,b2,h):
    return 0.5 * (b1 + b2) * h

#get user input for the base length and height of trapezoid
b1 = float(input("Enter 1st length for base: "))
b2 = float(input("Enter 2nd length for base: "))
h = float(input("Enter height of trapezoid: "))
#calculate and print the area of the trapezoid
area = trapezoid_area(b1,b2,h)
print(f"The area of guven trapezoid is {area:.2f}")

# Q.50]  Write a Python program to calculate the area of a parallelogram
#calculate the area of paralleglogram
def area_parallel(b,h):
    return b * h

#base of the length and height of parallelogram
b = float(input("Enter the length of base: "))
h = float(input("Enter height: "))

parallelogram = area_parallel(b,h)
print(f"The area of the parallelogram is {parallelogram:.2f}")#2f will give only 2 value after the period of main value

""" Q.51]  Write a Python program to calculate surface volume and area of a
cylinder """
#using math.pi we can get pi value
#thisfunction will find the volume of cylinder
def cal_volume(radius, height):
    return math.pi * radius**2 * height
#this function will find the surface area of cylinder
def cal_surface(radius, height):
    return 2 * math.pi * radius * (radius + height)
#this is the main function to take input from user as volume and surface area
def main():
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))

    volume = cal_volume(radius, height)
    surface_area = cal_surface(radius, height)

    print(f"The volume of cylinder is: {volume:.2f}")
    print(f"The surface area of the cylider is: {surface_area:.2f}")


if __name__ == "__main__":#here the program starts
    main()

# Q.52]  Write a Python program to returns sum of all divisors of a number.

user = int(input("Enter a number for divisors: ")) #divisors number are those integer that divides that number without remainder.
sum = 0
#this will loop from 1 to the user enterd input+1
for i in range(1,user+1):
    if user % i == 0:
        sum += i

print(f"Sum of all divisors of {user} is: {sum}: ")


""" Q.53]  Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers"""
#get user input and remove extra space using split() and converts into list of numbrers
num = input("Enter decimal number with spaces: ")
user_num = num.split()
#converts string number to float
main_num = list(map(float, user_num))
#using max() will give maximum number and using min() will give minimum
max_num = max(main_num)

min_num = min(main_num)

print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")