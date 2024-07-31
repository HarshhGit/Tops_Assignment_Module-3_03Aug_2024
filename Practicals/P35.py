# Q.35} Write a Python script to merge two Python dictionaries 

#using update()

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

merged_dict = dict1.copy()

merged_dict.update(dict2)

print("Merged dict of dict1 & dict2: ",merged_dict)

#using unpacking

merged_dict1 = {**dict1, **dict2}

print("Merged dictionary: ",merged_dict1)


#using '|' operator

merged_dict2 = dict1 | dict2

print("Merged dict: ",merged_dict2)









































