# Q.49]  Write a Python program to calculate the area of a trapezoid

def trapezoid_area(b1,b2,h):
    return 0.5 * (b1 + b2) * h


b1 = float(input("Enter 1st length for base: "))
b2 = float(input("Enter 2nd length for base: "))
h = float(input("Enter height of trapezoid: "))

area = trapezoid_area(b1,b2,h)
print(f"The area of guven trapezoid is {area:.2f}")