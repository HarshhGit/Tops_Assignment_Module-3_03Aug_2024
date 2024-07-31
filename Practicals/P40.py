# Q.40}  Write a Python program to find the highest 3 values in a dictionary

value = {'a': 5, 'b': 1, 'c': 9, 'd': 3, 'e': 7, 'f': 2}

sorted_value = sorted(value.values(), reverse=True)


highest_3 = sorted_value[:3]
print("Highest 3 value in dictionary are : ", highest_3)