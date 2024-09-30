#!/usr/bin/python3
"""
This module defines a function `class_to_json` that returns a dictionary
description with simple data structures for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj: An instance of a class.
    Returns:
        dict: A dictionary representation of the object.
    """
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (str, int, float, bool, list, dict))}
