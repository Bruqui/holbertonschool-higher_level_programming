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
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ['.', '?', ':']:
            result += "\n\n"
            i += 1
            # Skip any spaces following ., ?, and :
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    print(result, end="")
