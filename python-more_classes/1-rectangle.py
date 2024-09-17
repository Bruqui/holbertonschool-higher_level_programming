#!/usr/bin/python3
"""Defines a Rectangle class with private attributes width and heidht"""


class Rectangle:
    """
    Defines a rectangle with private instance attributes width and height
    """

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
