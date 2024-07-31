# Q.34}  Write a Python program to check multiple keys exists in a dictionary

def key_exist(dictionary, keys):
    return all(key in dictionary for key in keys)

dict1 = {'a':1, 'b':2,'c':3,'d':4}
key_check = ['a','b','e']

if key_exist(dict1,key_check):
    print("all keys exist in dictioary")
else:
    print("Not all keys exist in dictionary")