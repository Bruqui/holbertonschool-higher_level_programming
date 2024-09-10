#!/usr/bin/python3
"""
function that adds two numbers
"""


def add_integer(a, b=98):
    """Function that add two integer or float numbers

    Args:
        a: first number
        b: second number

    Return:
        The addition of two given numbers
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
