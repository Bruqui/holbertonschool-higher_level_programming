#!/usr/bin/python3
"""
This module defines a class Student.
"""


class Student:
    """
    A class to represent a student.
    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Args:
            attrs (list, optional): A list of strings representing attribute
            names.
            If provided, only attributes in this list will be retrieved.
        Returns:
            dict: A dictionary containing the student's information.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        return {attr: getattr(self, attr) for attr in attrs
                if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on a dictionary.
        Args:
            json (dict): A dictionary with the new values for the Student
            attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
