"""Q.7]. Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. """

squares = [i ** 2 for i in range(1, 31)]

first_5 = squares[:5]
print(f"Fist Five Squares between 1 to 30 are: {first_5}")

last_5 = squares[-5:]
print(f"Last Five Squares between 1 to 30 are: {last_5} ")