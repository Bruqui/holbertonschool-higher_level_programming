#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats, converting them to integers if necessary.

    Args:
        a: The first integer or float.
        b: The second integer or float, defaults to 98.

    Returns:
        The sum of a and b, as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
