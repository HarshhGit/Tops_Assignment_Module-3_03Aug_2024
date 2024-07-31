"""Q.18) Write a Python program to check whether an element exists within a tuple. """


main_tuple = (1, 2, "hello", True)

elem_check = "hello"

if elem_check in main_tuple:
    print(f"Emement '{elem_check}' exists in {main_tuple}")
else:
    print(f"Element '{elem_check}' doesn't exist in the {main_tuple}")