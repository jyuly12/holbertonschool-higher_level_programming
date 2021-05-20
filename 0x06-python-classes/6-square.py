#!/usr/bin/python3
"""
This module define a Square class
"""


class Square:
    """
    Define Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize Square class

        Args:
            size (int): size of square.
        """
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """
        Allows OOP functions.
        """
        return self.__size

    @property
    def position(self):
        """
        Allows OOP function.
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Value conditions.
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            print("\n" * self.position[1], end="")
            for i in range(self.__size):
                print(" " * self.position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
