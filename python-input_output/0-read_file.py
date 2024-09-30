#!/usr/bin/python3
"""
This module defines a function `read_file` that reads a UTF-8 encoded
text file and prints its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 encoded text file and prints its content to stdout.
    Args:
        filename (str): The name of the file to be read. Defaults to an
        empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
