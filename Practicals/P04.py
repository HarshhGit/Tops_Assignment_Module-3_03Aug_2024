# Q.4]. Write a Python program to remove duplicates from a list.


def remove_duplicate(n):
    n = set(n)
    print(n)

user = input("Enter number using space: ")

user_numbers = [int(num) for num in user.split()]

remove_duplicate(user_numbers)



"""We can remove duplicate value using typecasting by 
converting list into set that don't allow duplicate values"""