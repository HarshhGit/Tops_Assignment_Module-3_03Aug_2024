# Q.16) Write a Python program to create a tuple with numbers. 

user = input("Enter number with spaces: ")
print("number without tuple", user)

num = user.split()

num_list = [int(i) for i in num]

num_tuple = tuple(num_list)

print("Numbers with tuple: ", num_tuple)

