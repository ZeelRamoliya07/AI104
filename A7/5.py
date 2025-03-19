"""
Create a base class "Shape" with methods to calculate the area and perimeter. Implement
derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area
and perimeter calculations.
"""

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

def shape_menu():
    print("\n1. Rectangle")
    print("2. Circle")
    
    choice = input("Choose Shape: ")

    if choice == '1':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        rect = Rectangle(length, width)
        print("Area:", rect.area())
        print("Perimeter:", rect.perimeter())

    elif choice == '2':
        radius = float(input("Enter radius: "))
        circ = Circle(radius)
        print("Area:", circ.area())
        print("Perimeter:", circ.perimeter())

    else:
        print("Invalid choice!")

shape_menu()
