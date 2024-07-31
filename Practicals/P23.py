# Q.23) Write a Python program to find the repeated items of a tuple. 

tuple1 = (1,2,3,4,5,6,1,4,5,7,2,3)
print("main tuple: ", tuple1)

count = {}

for i in tuple1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

repeted_val = [i for i, val in count.items() if val > 1]
repeted_val = tuple(repeted_val)

print("Repeated items: ", repeted_val)