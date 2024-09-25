#!/usr/bin/python3

class Fish:
    """
    Represents a Fish, which can swim and has a specific habitat.
    """

    def swim(self):
        """
        Print a message indicating the fish is swimming.
        """
        print("The fish is swimming.")

    def habitat(self):
        """
        Print a message describing the fish's habitat.
        """
        print("The fish lives in water.")


class Bird:
    """
    Represents a Bird, which can fly and has a specific habitat.
    """

    def fly(self):
        """
        Print a message indicating the bird is flying.
        """
        print("The bird is flying.")

    def habitat(self):
        """
        Print a message describing the bird's habitat.
        """
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """
    Represents a Flying Fish, which can swim like a fish and fly like a bird.
    The Flying Fish has its own behaviors for flying, swimming, and its
    habitat.
    """

    def swim(self):
        """
        Override the swim method to describe the unique swimming behavior of a
        flying fish.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Override the fly method to describe the unique flying behavior of a
        flying fish.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Override the habitat method to describe the unique habitat of a flying
        fish.
        """
        print("The flying fish lives both in water and the sky!")
