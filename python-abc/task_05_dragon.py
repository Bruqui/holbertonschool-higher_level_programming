#!/usr/bin/python3

class SwimMixin:
    """
    A mixin class that provides swimming functionality.
    """

    def swim(self):
        """
        Print a message indicating that the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying functionality.
    """

    def fly(self):
        """
        Print a message indicating that the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits swimming and flying capabilities from
    SwimMixin and FlyMixin.
    Additionally, it can roar.
    """

    def roar(self):
        """
        Print a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
