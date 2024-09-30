#!/usr/bin/python3
"""
This module defines a function `append_write` that appends a string to a
UTF-8 encoded text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF-8 encoded text file and returns the number
    of characters added.
    Args:
        filename (str): The name of the file to append to. Defaults to an
        empty string.
        text (str): The text to be appended to the file. Defaults to an
        empty string.
    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
