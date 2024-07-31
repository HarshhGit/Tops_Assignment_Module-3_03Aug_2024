# Q.12] Write a Python program to select an item randomly from a list. 

import random


fruits = ["apple","banana","cherry","orange"]

random_item = random.choice(fruits)

print("Fruits store: ", fruits)
print("Rnadomly selected items from fruits store: ", random_item)