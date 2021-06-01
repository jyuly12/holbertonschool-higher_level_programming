#!/usr/bin/python3
"""
This module defines the Student class
"""


class Student:
    """
    Defines Student class

    Args:

        first_name (str): first name of the student
        last_name (str): last name of the student
        age (int): age of the student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
        attrs (list of strings)
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}

        if type(attrs) is list:
            for i in attrs:
                if i in self.__dic__:
                    new_dict[i] = self.__dict__[i]

        return new_dict
