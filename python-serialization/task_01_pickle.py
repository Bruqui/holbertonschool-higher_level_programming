#!/usr/bin/python3
"""
This module defines a custom Python class named CustomObject which can
serialize its instances using the pickle module and deserialize them to
recreate the object.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with attributes name, age, and
    is_student.
    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Boolean indicating if the person is a student.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes an instance of CustomObject with the given attributes.
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the CustomObject instance in a readable
        format.
        """
        print("name: {}".format(self.name))
        print("age: {}".format(self.age))
        print("is_student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance of CustomObject and saves it to a
        file.
        Args:
            filename (str): The name of the file where the object will be
            saved.
        Raises:
            IOError: If an error occurs while writing to the file.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject from the given file.
        Args:
            filename (str): The name of the file from which to load the
            object.
        Returns:
            CustomObject: An instance of CustomObject loaded from the file,
                          or None if an error occurs.
        Raises:
            IOError: If the file does not exist or there is a read error.
            pickle.UnpicklingError: If the file contains malformed or invalid
                                    data.
        """
        with open(filename, 'rb') as f:
            return pickle.load(f)
