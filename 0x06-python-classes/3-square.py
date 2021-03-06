#!/usr/bin/python3
"""
This module define a Square class
"""


class Square:
    """
    Define Square class
    """
    def __init__(self, size=0):
        """
        Initialize Square class

        Args:
            size (int): size of square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Obtain Square area
        """
        return self.__size ** 2
