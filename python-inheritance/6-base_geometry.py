#!/usr/bin/python3
"""
Module that defines a class BaseGeometry with a method that raises an
exception.
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
