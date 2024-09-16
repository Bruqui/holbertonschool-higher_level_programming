#!/usr/bin/python3
"""
This module defines a Square class with private instance attributes `size`
and `position`, getter and setter methods for both attributes, and methods to
calculate the area and print the square
"""


class Square:
    """
    This class represents a square with private instance attributes `size`
    and `position`. It includes getter and setter methods for these attributes,
    a method to calculate the area of the square, and a method to print the
    square using `#`
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with the size and position The size defaults to 0
        and the position defaults to (0, 0). Both attributes are validated

        Args:
            size (int, optional): The size of the square. Defaults to 0
            position (tuple, optional): The position of the square (x, y)
                                        Defaults to (0, 0)

        Raises:
            TypeError: If size is not an integer or position is not tuple of 2
                       positive integers
            ValueError: If size is less than 0 or any element of position is
                        less than 0
        """
        self.size = size
        self.position = position

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
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The new position of the square (x, y).

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If any element of position is less than 0.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character `#`. If size is 0, it prints an
        empty line. The position attribute determines the indentation from
        the left and top margins.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
