#!/usr/bin/python3

from typing import Iterable


class VerboseList(list):
    """
    A custom list class that extends Python's built-in list.
    It prints a notification message every time an item is added or removed
    using the append, extend, remove, or pop methods.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a notification.
        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """
        Extend the list by appending elements from the iterable and print a
        notification.
        Args:
            item (iterable): The item to be added to the list.
        """
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """
        Remove the first occurrence of the item from the list and print a
        notification.
        Args:
            item: The item to be removed from the list.
        Raises:
            ValueError: If the item is not present in the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given index and print a notification
        Args:
            index (int, optional): The index of the item to be removed.
            Defaults to -1 (the last item).
        Return:
            The item that was removed from the list.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
    