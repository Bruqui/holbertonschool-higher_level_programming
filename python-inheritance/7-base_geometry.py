#!/usr/bin/python3
"""
Module that defines a class BaseGeometry with methods for geometry calculations.
"""


class BaseGeometry:
    """
    Class representing BaseGeometry.
    """
    def area(self):
        """
        Raises an Exception with the message: area() is not implemented.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that the value is an integer and greater than 0.
        Args:
            name (str): The name of the parameter (assumed to always be a
            string).
            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
