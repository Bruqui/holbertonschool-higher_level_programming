#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute `size`,
getter and setter methods for size, and a method to calculate the square area
"""


class Square:
    """
    This class represents a square with a private instance attribute `size`
    It includes getter and setter methods for size and a method to calculate
    the area of the square
    """

    def __init__(self, size=0):
        """
        Initialize the square with the size which is optional and defaults to 0
        The size attribute must be an integer and greater than or equal to 0

        Args:
            size (int, optional): The size of the square. Defaults to 0

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square

        Returns:
            int: The size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
