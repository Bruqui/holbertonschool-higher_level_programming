#!/usr/bin/python3
"""
This module defines a function `save_to_json_file` that writes a Python
object to a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using a JSON representation.
    Args:
        my_obj: The Python object to be serialized to JSON.
        filename (str): The name of the file to write the JSON data to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)