""" Q.53]  Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers"""

num = input("Enter decimal number with spaces: ")
user_num = num.split()

main_num = list(map(float, user_num))

max_num = max(main_num)

min_num = min(main_num)

print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")