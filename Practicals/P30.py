# Q.30} Write a Python script to check if a given key already exists in a dictionary. 

ex_dict = {'apple':5, 'banana':3,'cherry':7,'orange':2}

def key_exists(dictionary,key):
    if key in dictionary:
        print(f"{check_key}'key' exists in the dictionary.")
    else:
        print(f"{check_key}'key' does not exist in the dictionary.")


check_key = 'apple'
key_exists(ex_dict,check_key)

check_key = 'mango'
key_exists(ex_dict,check_key)