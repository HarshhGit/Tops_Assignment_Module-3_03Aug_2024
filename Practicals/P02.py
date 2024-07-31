"""Q.2]. Write a Python function to get the largest number, smallest num and sum
of all from a list."""

def calculate(n):
    if not n:
        return None, None, None
    largest = max(n)
    smallest = min(n)
    total_sum = sum(n)
    Ans = f"Largest = {largest} Smallest = {smallest} Total = {total_sum}"
    print(Ans)
    return largest, smallest, total_sum

user = input("Enter number using space: ")

user_numbers = [int(num) for num in user.split()]

calculate(user_numbers)