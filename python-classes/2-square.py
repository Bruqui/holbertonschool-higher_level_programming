#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute 'size'
and instantiation with an optional size
"""


class Square:
    """
    This class represents a square with a private instance attribute 'size'
    """

    def __init__(self, size=0):
        """
        Initialize the square with the size which is optional and defaults to 0
        The size attribute must be an integer and greater than or equal to 0

        Args:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
