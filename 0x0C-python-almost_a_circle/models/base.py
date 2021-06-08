#!/usr/bin/python3
"""
This module contains the base class
"""


class Base:
    """
    Creates de Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base class.

        Args:
        id (int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
