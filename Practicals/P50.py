# Q.50]  Write a Python program to calculate the area of a parallelogram

def area_parallel(b,h):
    return b*h

b = float(input("Enter the length of base: "))
h = float(input("Enter height: "))

parallelogram = area_parallel(b,h)
print(f"The area of the parallelogram is {parallelogram:.2f}")

