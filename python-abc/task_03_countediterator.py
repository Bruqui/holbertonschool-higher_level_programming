#!/usr/bin/python3

class CountedIterator:
    """
    A custom iterator that extends the functionality of a standard iterator
    by keeping track of the number of items that have been iterated over.
    Attributes:
        iterator (iterator): The original iterator created from an iterable.
        count (int): Counter to track the number of items fetched from the
        iterator.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable and set the counter
        to 0.
        Args:
            iterable (iterable): The iterable to be wrapped by the iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the count.
        Returns:
            The next item from the original iterator.
        Raises:
            StopIteration: When there are no more items to iterate.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Return the number of items that have been iterated over so far.
        Returns:
            int: The number of items that have been fetched.
        """
        return self.count

    def __iter__(self):
        """
        Return the iterator object itself.
        This allows the CountedIterator to be used in a loop or other contexts
        that expect an iterator.
        Returns:
            CountedIterator: The current instance of the CountedIterator.
        """
        return self
