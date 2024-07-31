# Q.22) Write a Python program to replace last value of tuples in a list.


tuple_list = [(1,2,3),(4,5,6),(7,8,9)]
print("Main tuple: ", tuple_list)

replace_val = 1

updated_tuple_list = []

for t in tuple_list:
    updated_tuple = t[:-1] + (replace_val,)
    updated_tuple_list.append(updated_tuple)

print("After replacing last value: ",updated_tuple_list)