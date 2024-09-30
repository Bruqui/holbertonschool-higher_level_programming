#!/usr/bin/python3
"""
This module defines a function `from_json_string` that returns a Python
data structure (object) represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python data structure from a JSON string.
    Args:
        my_str (str): The JSON string to be converted into a Python object.
    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
