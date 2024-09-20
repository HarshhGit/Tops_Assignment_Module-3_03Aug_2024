"""Q.1]. How will you remove last object from a list?
Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?"""

list1 = [2, 33, 222, 14, 25]

#To remove last object from list we can use pop() method that removes last object if parameter isn't given
#Right now list1 [-1] object is 25 without removing object 

rem = list1.pop()

print("Removed last object", rem)
print("After using pop()", list1)

#after using pop() new object at [-1] index is 14

"""Q.2]. Write a Python function to get the largest number, smallest num and sum
of all from a list."""

def calculate(n):
#check if argument is empty or not
    if not n:
        return None, None, None
#used built-in functions like max(),min(),sum() to find largest smallest and total of list
    largest = max(n)
    smallest = min(n)
    total_sum = sum(n)
    Ans = f"Largest = {largest} Smallest = {smallest} Total = {total_sum}"
    print(Ans)
    return largest, smallest, total_sum

user = input("Enter number using space: ")
user_numbers = []#creates empty list to store user input 
for num in user.split():
    user_numbers.append(int(num)) #all given input will be stored after split() by space.

calculate(user_numbers)

"""Q.3]. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings."""

user = ['abc', 'xyz', 'aba', '1221','aba']
count = 0
same = []

for i in user :
    #check length of string is greater than or equal to 2 and last character of string are same using indexing 
    #and operator need to be both True else it give false
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1
        same.append(i)
print(f"Fisrt and last same char string: {same}")
print(f"Number of Matching String: {count} ")

# Q.4]. Write a Python program to remove duplicates from a list.

"""We can remove duplicate value using typecasting by
converting list into set that don't allow duplicate values"""
def remove_duplicate(n):
    n = set(n)
    print(n)
#get user input and convert into list
user = input("Enter number using space: ")
user_numbers = [int(num) for num in user.split()]

remove_duplicate(user_numbers)
#by calling the function it will take input and than removes duplicates



# Q.5] Write a Python program to check a list is empty or not


list1 = [5]
# used 'not' to check if the list contain anything or its empty
if not list1:
    print("The list is empty")
else:
    print("The list is not empty")

# Q.6] #find common elements from two list

def common(list1, list2):
    common_mem = []
#iterates each elements one by one
    for member in list1:
#if the element is present in the second list it will append into empty list
        if member in list2:
            common_mem.append(member)
#if common elements are found returns true and the common elements
    if common_mem:
        return True, common_mem
    else:
        return False

list1 = [22, 25, 15, 24, 16, 45]
list2 = [14, 18, 16, 10, 17, 50]

print(common(list1, list2)) 

"""Q.7]. Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. """
#it creates squares of numbers in range of 1 to 30 in loop -1 so we need to go 31 to reach 30
squares = [i ** 2 for i in range(1, 31)]
#gives first file elem from list using indexing
first_5 = squares[:5]
print(f"Fist Five Squares between 1 to 30 are: {first_5}")
#using nagetive indexing gives last elem
last_5 = squares[-5:]
print(f"Last Five Squares between 1 to 30 are: {last_5} ")

""" Q.8] Write a Python function that takes a list and returns a new list with unique
elements of the first list. """

#using typecasting to remove duplicate and than again converting into list

def unique_elm(l):
    l = list(set(l))
    return l


list1 = [10,20,15,25,10,30]
print(f"First list without unique elements: {list1}")

print("List with unique elements: " ,unique_elm(list1))


# Q.9]. Write a Python program to convert a list of characters into a string. 


list1 = ['H','A','R','S','H']

str1 = ''.join(list1)

print(str1)

#---->'' empty string before join() method for no space between charachter


# Q.10] Write a Python program to select an item randomly from a list. 

import random

#from random module used random.choice that gives random elem from list
list1 = [1,2,3,4,5,6,7]

random_num = random.choice(list1)
print("list1: ",list1)
print("Random number from list1: ",random_num)


# Q.11]  Write a Python program to find the second smallest number in a list.


list1 = [10,5,20,30]
#checks if list have less than 2 elem to give error
if len(list1) < 2:
    print("List isn't correct!!!")
else:
#using sort() method we can change the order into ascending order from smallest to largest
    second_small = list1
    second_small.sort()
    #after sorting accessing Second smallest elem using indexing
    print ("Second smallest number is: ",second_small[1])


# Q.12] Write a Python program to select an item randomly from a list. 



#using random.choice() to select a random element from the list
fruits = ["apple","banana","cherry","orange"]

random_item = random.choice(fruits)

print("Fruits store: ", fruits)
print("Rnadomly selected items from fruits store: ", random_item)



# Q.13] Write a Python program to check whether a list contains a sub list.


list1 = [1,2,3,4,5,6]
sub_list = [4,5,6]

list1_len = len(list1)
sub_len = len(sub_list)

count = 0
#loop to the main list to check for the sublist
for i in range(list1_len - sub_len + 1):
#check if the both posrton of list and sublist are same or not 
    if list1[i:i + sub_len] == sub_list:
        count = 1
        break
#if count changes from 0 to 1 it has sublist else false
if count:
    print("The list1 conatins sublist.")
else:
    print("List1 doesn't contain sublist.")


# Q.14]  Write a Python program to split a list into different variables. 

list1 = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
#given variables as per the values and unpacked into them
day1, day2, day3, day4, day5, day6, day7, = list1

print("splited list into variables:")

print("Today is: ",day1)
print("Today is: ",day2)
print("Today is: ",day3)
print("Today is: ",day4)
print("Today is: ",day5)
print("Today is: ",day6)
print("Today is: ",day7)

# Q.15) Write a Python program to create a tuple with different data types. 

#tuple are immutable

tuple1 = (1, "harsh", 3.14, True,[1,2,3],{"key":"value"})


print("Tuple with different data types: ", tuple1)
print("Type of tuple1: ",type(tuple1))
#one by one it give type of each elem
for i in tuple1:
    print(f"value: {i}, Type: {type(i)}")

# Q.16) Write a Python program to create a tuple with numbers. 

user = input("Enter number with spaces: ")
print("number without tuple", user)

num = user.split()

num_list = [int(i) for i in num]
#type casting to convert list into tuple
num_tuple = tuple(num_list)

print("Numbers with tuple: ", num_tuple)

# Q.17) Write a Python program to convert a tuple to a string.

#used join method to convert the tuple elem into a string 
tuple1 = (1, 2, "hello", 3.14)
#map() method is used to iterate items into tuple,list etc and returns new iterable to transformation without using loop
str1 = ' '.join(map(str,tuple1))

print(str1, type(str1))

"""Q.18) Write a Python program to check whether an element exists within a tuple. """


main_tuple = (1, 2, "hello", True)
#elem to check 
elem_check = "hello"
#in operator is used to check if given condition is True or False
if elem_check in main_tuple:
    print(f"Emement '{elem_check}' exists in {main_tuple}")
else:
    print(f"Element '{elem_check}' doesn't exist in the {main_tuple}")

# 19) Write a Python program to find the length of a tuple.


ex = ("hello", 5, 22, True, 3.14, None)
#len() is used to get the length of thetuple how many elem cotains
print(len(ex))


# Q.20)  Write a Python program to convert a list to a tuple.


list1 = ["hello", 22, 3.14, True, None]
print("list as list1 before typecasting: ", list1)

#typecasting list into tuple

tuple1 = tuple(list1)
print("list as tuple1 after typecasting: " ,tuple1)