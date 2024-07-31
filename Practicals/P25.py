# Q.25) Write a Python program to unzip a list of tuples into individual lists 

tuple_list = [(1,0), (2,1),(3,2)]

list1, list2 = zip(*tuple_list)

list1 = list(list1)
list2 = list(list2)

print("list 1: ", list1)
print("list 2: ",list2)