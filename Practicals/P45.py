# Q.45]Write a Python function to check whether a number is perfect or not.


def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum = sum + i

    if sum == n:
        return (f"Yes {n} is a perfect number")
    else:
        return(f"{n} isn't a perfect number")

user = int(input("Enter a number to check perfect or not: "))

print(perfect(user))

