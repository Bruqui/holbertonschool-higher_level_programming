/usr/bin/python3
"""
This module provides a function that returns a list of attributes and methods
of an object
"""


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.
    Returns:
        A list of strings representing the attributes and methods of the object
    """
    return dir(obj)
