# Q.15) Write a Python program to create a tuple with different data types. 

tuple1 = (1, "harsh", 3.14, True,[1,2,3],{"key":"value"})


print("Tuple with different data types: ", tuple1)
print("Type of tuple1: ",type(tuple1))

for i in tuple1:
    print(f"value: {i}, Type: {type(i)}")