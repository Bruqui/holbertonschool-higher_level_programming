#!/usr/bin/python3
"""
Module that defines the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class,
    but not an instance of a_class itself. Otherwise, returns False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
