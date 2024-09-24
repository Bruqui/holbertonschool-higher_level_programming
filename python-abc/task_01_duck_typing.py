#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    This class defines the interface for shapes, enforcing the implementation
    of area and perimeter methods in subclasses.
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that represents a circle.
    Inherits from Shape and implements the area and perimeter methods.
    Attributes:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius):
        """
        Initialize the Circle with a given radius.
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    Rectangle class that represents a rectangle.
    Inherits from Shape and implements the area and perimeter methods.
    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize the Rectangle with a given width and height.
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Print the area and perimeter of a given shape object using duck typing.
    This function assume that the passed object has both 'area' and
    'perimeter' methods.
    Args:
        shape (Shape): An object that implements the Shape interface (i.e.,
        has 'area' and 'perimeter' methods).
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))