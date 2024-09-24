#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class for all animals.
    This class defines the interface for animal classes, ensuring that all
    subclasses implement the 'sound' method.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that should return the sound the animal makes.
        Returns:
            str: The sound of the animal.
        """
        pass

class Dog(Animal):
    """
    Dog class that represents a dog.
    Inherits from Animal and implements the 'sound' method.
    """

    def sound(self):
        """
        Returns the sound that a dog makes.
        Returns:
            str: The sound 'Bark'.
        """
        return "Bark"
    
class Cat(Animal):
    """
    Cat class that represents a cat.
    Inherits from Animal and implements the 'sound' method.
    """

    def sound(self):
        """
        Returns the sound that a cat makes.
        Returns:
            str: The sound 'Meow'.
        """
        return "Meow"
