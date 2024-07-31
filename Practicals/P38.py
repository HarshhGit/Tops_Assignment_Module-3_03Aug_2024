# Q.38}  Write a Python program to print all unique values in a dictionary. 


dict1 = {'a':1,'b':2,'c':3,'d':4}

unique = set(dict1.values())

print("Unique values from dictionary: ", unique)