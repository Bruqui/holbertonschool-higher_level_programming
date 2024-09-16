#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute 'size'
"""


class Square:
    """
    This class represents a square with a private instance attribute 'size'
    """

    def __init__(self, size):
        """
        Initialize the square with the size.
        The size attribute is private to ensure control over its value

        Args:
            size: The size of the square
        """
        self.__size = size
