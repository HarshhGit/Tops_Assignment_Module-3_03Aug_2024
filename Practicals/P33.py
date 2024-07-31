"""Q.33} Write a Python script to print a dictionary where the keys are numbers
between 1 and 15."""

num = {}

for i in range(1,15+1):
    num[i] = i ** 2

print(num)