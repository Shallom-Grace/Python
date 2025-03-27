"""
This Python program defines a Circle class that calculates 
the area and circumference of a circle based on a given radius. 
It prompts the user to input a radius, then creates a Circle object 
to compute and display the area and circumference.
"""

import math  # Importing the math module for mathematical operations

# Defining a class named 'Circle' to represent a geometric circle
class Circle:
    def __init__(self, radius):
        #Constructor to initialize the radius of the circle
        self.radius = radius

    def getArea(self):
        #Method to calculate and return the area of the circle
        return math.pi * self.radius ** 2

    def getCircumference(self):
        #Method to calculate and return the circumference of the circle
        return math.pi * (self.radius * 2)


# Taking user input for the radius and converting it to a float
radius = float(input("Input the radius of the circle: "))

# Creating an object of the Circle class with the given radius
circle_obj = Circle(radius)

# Calculating the area of the circle
area = circle_obj.getArea()

# Calculating the circumference (perimeter) of the circle
perimeter = circle_obj.getCircumference()

# Displaying the calculated area and perimeter
print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)