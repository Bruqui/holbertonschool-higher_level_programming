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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the student's information.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
