#!/usr/bin/python3
"""
This script defines a function that prints text with 2 new lines
after certain characters.
"""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?', and ':'.

    Parameters:
    text (str): The text to be processed. Must be a string.

    Raises:
    TypeError: If text is not a string.
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        i = 0
        for char in text:
            if i == 0:
                if char == " ":
                    continue
                else:
                    i = 1
            if i == 1:
                if char in [".", "?", ":"]:
                    print(char + "\n")
                    i = 0
                else:
                    print(char, end="")
