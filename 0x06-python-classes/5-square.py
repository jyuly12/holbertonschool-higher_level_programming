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
        self.__size = size

    @property
    def size(self):
        """
        Allows OOP functions.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Value conditions.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Obtain Square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square.
        """
        if self.__size == 0:
            print("")
            return
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
