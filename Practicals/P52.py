# Q.52]  Write a Python program to returns sum of all divisors of a number.

user = int(input("Enter a number for divisors: "))
sum = 0
for i in range(1,user+1):
    if user % i == 0:
        sum += i

print(f"Sum of all divisors of {user} is: {sum}: ")