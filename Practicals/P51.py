""" Q.51]  Write a Python program to calculate surface volume and area of a
cylinder """

import math

def cal_volume(radius, height):
    return math.pi * radius**2 * height

def cal_surface(radius, height):
    return 2 * math.pi * radius * (radius + height)

def main():
    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))

    volume = cal_volume(radius, height)
    surface_area = cal_surface(radius, height)

    print(f"The volume of cylinder is: {volume:.2f}")
    print(f"The surface area of the cylider is: {surface_area:.2f}")


if __name__ == "__main__":
    main()

