# Q.21) Write a Python program to reverse a tuple.

tuple1 = ('hello', 22, 3.14, True, None)

rev = tuple1[::-1]
print("Reversed tuple using indexing: ", rev)


#using for loop with len()
rev_tuple = []
for i in range(len(tuple1)-1,-1,-1):
    rev_tuple.append(tuple1[i])
rev_i = tuple(rev_tuple)
    
print("Reversed tuple using for loop: ", rev_i)


