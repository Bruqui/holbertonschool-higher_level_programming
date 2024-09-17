#!/usr/bin/python3
"""
Defines a Rectangle class with private attributes width and height,
public methods for area and perimeter, string representation for print()
and eval(), a class attribute to track the number of instances,
and prints a message on deletion.
"""


class Rectangle:
    """
    Defines a rectangle with private instance attributes width and height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with optional width and height (default is 0)
        Args:
            width (int): width of the rectangle, must be >= 0
            height (int): height of the rectangle, must be >= 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args:
            value (int): The width value to set
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Args:
            value (int): The height value to set
        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle
        If either width or height is 0, the perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the character #
        If either width or height is 0, it returns an empty string
        Returns:
            str: A string representing the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used
        to recreate a new instance with eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
     
    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
