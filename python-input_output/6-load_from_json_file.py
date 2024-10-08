#!/usr/bin/python3
"""
This module defines a function `load_from_json_file` that creates a
Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.
    Args:
       filename (str): The name of the JSON file to be read.
    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
