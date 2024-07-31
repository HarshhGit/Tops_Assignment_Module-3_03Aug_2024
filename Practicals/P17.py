# Q.17) Write a Python program to convert a tuple to a string.


tuple1 = (1, 2, "hello", 3.14)

str1 = ' '.join(map(str,tuple1))

print(str1, type(str1))