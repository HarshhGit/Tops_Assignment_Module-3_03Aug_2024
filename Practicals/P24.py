# Q.24)  Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple1 = [(1,2,3), (), (4,5,6)]

updated_tuple = [t for t in tuple1 if t]
print("Tuple list without empty tuple: ",updated_tuple)



