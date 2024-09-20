# Q.21) Write a Python program to reverse a tuple.

tuple1 = ('hello', 22, 3.14, True, None)
#using indexing
rev = tuple1[::-1]
print("Reversed tuple using indexing: ", rev)


#using for loop with len()
rev_tuple = []
for i in range(len(tuple1)-1,-1,-1):
    rev_tuple.append(tuple1[i])
rev_i = tuple(rev_tuple)
    
print("Reversed tuple using for loop: ", rev_i)

# Q.22) Write a Python program to replace last value of tuples in a list.


tuple_list = [(1,2,3),(4,5,6),(7,8,9)]
print("Main tuple: ", tuple_list)
#value to replace the last elem in all tuple item
replace_val = 1
#list to store updated tuple
updated_tuple_list = []

for t in tuple_list:
    #replace the last value using index and adds
    updated_tuple = t[:-1] + (replace_val,)
    updated_tuple_list.append(updated_tuple)

print("After replacing last value: ",updated_tuple_list)


# Q.23) Write a Python program to find the repeated items of a tuple. 

tuple1 = (1,2,3,4,5,6,1,4,5,7,2,3)
print("main tuple: ", tuple1)

count = {} #empty dict to count numbers repeated
#this for loop will go one by one all item into tuple
for i in tuple1:
    if i in count:
        count[i] += 1 #this will increse the count if same item reapeted by 1
    else:
        count[i] = 1 #this will give 1 if any item appears one time 

repeted_val = [i for i, val in count.items() if val > 1]
repeted_val = tuple(repeted_val)

print("Repeated items: ", repeted_val)

# Q.24)  Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple1 = [(1,2,3), (), (4,5,6)]
updated_tuple = [] #empty list to store updated tuple
for t in tuple1:
    if t:
        updated_tuple.append(t)

print("tuple list without empty tuple: ",updated_tuple)

# Q.25) Write a Python program to unzip a list of tuples into individual lists 

tuple_list = [(1,0), (2,1),(3,2)]
#ihis will unzip the tuples into two separate lists
list1, list2 = zip(*tuple_list)
#convert the tuples into list
list1 = list(list1)
list2 = list(list2)

print("list 1: ", list1)
print("list 2: ",list2)

# Q.26}  Write a Python program to convert a list of tuples into a dictionary. 

tuple_list = [(1,0), (2,1),(3,2)]
#converts list of tuples into dict after typecasting
dict1 = dict(tuple_list)
print(dict1, type(dict1))


# Q.27}  How will you create a dictionary using tuples in python?


dict_tuple = {('sunday',1),('monday',2),('tuesday',3)}
#by type casting it will convert set of tuple into key and value pair as dictionary
dict1 = dict(dict_tuple)

print(dict1,type(dict1))

# Q.28}  Write a Python script to sort (ascending and descending) a dictionary by value. 

days = {'tuesday':3, 'sunday':1, 'monday':2}
#it will sort the dictionary by its value in ascendig
asc_dic = dict(sorted(days.items(), key=lambda item: item[1]))
#this will sort dictionary by its value in descending using reverse=True
desc_dic = dict(sorted(days.items(), key = lambda item: item[1],reverse=True))

print("Dictionary with ascending order: ")
print(asc_dic)

print("\nDictionary with descending order: ")
print(desc_dic)

# Q.29} Write a Python script to concatenate following dictionaries to create a new one. 

dict1 = {'a':1, 'b':2 }
dict2 = {'c':3, 'd':4}
dict3 = {'e':5, 'f':6}
#unpacking the dictionary to concatenate all dictionary
concat_dict = {**dict1, **dict2, **dict3}

print("Concatenated dictionary: ")
print(concat_dict)

# Q.30} Write a Python script to check if a given key already exists in a dictionary. 

ex_dict = {'apple':5, 'banana':3,'cherry':7,'orange':2}
#this function will provide output as exist in dict if it have in the dictionary else does not from argument
def key_exists(dictionary,key):
    if key in dictionary:
        print(f"{check_key}'key' exists in the dictionary.")
    else:
        print(f"{check_key}'key' does not exist in the dictionary.")


check_key = 'apple'
key_exists(ex_dict,check_key)

check_key = 'mango'
key_exists(ex_dict,check_key)

# Q.31} How Do You Traverse Through A Dictionary Object In Python? 

clas = {
    "stud1": 1,
    "age": 21,
    "address": "maninagar"
}
#this will only print keys from dict
for h in clas:
    print("\nGive only keys as output: ",h) 
#this will print keys and values as tuple form from dict
for i in clas.items():
    print("\nGives keys and values as tuple output:" ,i)
#giving two variable in for loop will work as key and values and will give separately paris of key values
for g,n in clas.items():
    print("\nGives both key and values as output: ",g,n)

# Q.32}  How Do You Check The Presence Of A Key In A Dictionary?


sample_dict = {
    'apple':5,
    'banana':3,
    'cherry':4,
    'orange':6
}

key_check = 'banana'

#it will check if give key_check exist in sample_dict 
if key_check in sample_dict:
    print(f"Key'{key_check}' exists in dictionary.")
else:
    print(f"Key '{key_check}' does not exists in the dictionary.")

"""Q.33} Write a Python script to print a dictionary where the keys are numbers
between 1 and 15."""

num = {} #Empty dictionary to store number as key and values as squares 
#this will iterate from 1 to 15 and give squares of number in i
for i in range(1,15+1):
    num[i] = i ** 2

print(num)

# Q.34}  Write a Python program to check multiple keys exists in a dictionary

#It will check if all the keys are exist in main dictionary if yes true else false
def key_exist(dictionary, keys):
    return all(key in dictionary for key in keys)

dict1 = {'a':1, 'b':2,'c':3,'d':4}
key_check = ['a','b','e']

if key_exist(dict1,key_check):
    print("all keys exist in dictioary")
else:
    print("Not all keys exist in dictionary")

# Q.35} Write a Python script to merge two Python dictionaries 

#using update()

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

merged_dict = dict1.copy()
merged_dict.update(dict2)
print("Merged dict of dict1 & dict2: ",merged_dict)

#using unpacking to merge two different dict
merged_dict1 = {**dict1, **dict2}
print("Merged dictionary: ",merged_dict1)
#using '|' operator we can merge dictionary
merged_dict2 = dict1 | dict2
print("Merged dict: ",merged_dict2)

# Q.36}  Write a Python program to map two lists into a dictionary 

list1 = [1,2,3,4]
list2 = [5,6,7,8]
#by zip we can give key and values and after that we can change its type into dictionary
zip1 = zip(list1,list2)

print("mapped dictionary: ",dict(zip1))


""" Q.37}  Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}). """

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}

combine1 = Counter(d1)
combine2 = Counter(d2)
#it will total the value of common keys
total_value = combine1 + combine2

print("Total of both dictionary: ", total_value)

# Q.38}  Write a Python program to print all unique values in a dictionary. 


dict1 = {'a':1,'b':2,'c':3,'d':4}
#converted into set so we get unique values
unique = set(dict1.values())

print("Unique values from dictionary: ", unique)


""" Q.39}  Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd """
from itertools import product

dict1 = {'1': ['a','b'], '2': ['c','d']}
#we will get all the combinations of dictionary using product
combinations = product(*dict1.values())
#one by one to all the combinations
for combination in combinations:
    print("Unique values from dictionary: ", ''.join(combination))

# Q.40}  Write a Python program to find the highest 3 values in a dictionary

value = {'a': 5, 'b': 1, 'c': 9, 'd': 3, 'e': 7, 'f': 2}
#sorted() will sort the values and it will be in descending order using reverse = True
sorted_value = sorted(value.values(), reverse=True)


highest_3 = sorted_value[:3]
print("Highest 3 value in dictionary are : ", highest_3)