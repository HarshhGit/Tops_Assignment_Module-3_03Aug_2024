# Q.32}  How Do You Check The Presence Of A Key In A Dictionary?


sample_dict = {
    'apple':5,
    'banana':3,
    'cherry':4,
    'orange':6
}

key_check = 'banana'

if key_check in sample_dict:
    print(f"Key'{key_check}' exists in dictionary.")
else:
    print(f"Key '{key_check}' does not exists in the dictionary.")