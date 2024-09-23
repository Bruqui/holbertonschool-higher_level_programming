#!/usr/bin/python3
"""
Module that defines a class MyList, which inherits from the built-in list.
"""


class MyList(list):
    """
    Class MyList that inherits from list and adds a method to print sorted
    """
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
