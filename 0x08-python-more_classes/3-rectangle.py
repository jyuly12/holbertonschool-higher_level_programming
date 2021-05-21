#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    creates a class
    """
    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle class
        Args:

            width (int): size of the Rectangle.

            height (int): size of the Rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Returns a width instance
        """
        return self.__weith

    @property
    def height(self):
        """
        Returns a height instance
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Define width conditions
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Define height conditions
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Obtain the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Obtain the rectangle perimeter
        """
        a = self.__height
        b = self.__width
        if a == 0 or b == 0:
            return 0
        return 2 * (a + b)

    def __str__(self):
        """
        generate a printeable rectangle
        """
        a = self.__height
        b = self.__width

        if a is 0 or b is 0:
            return ""

        str = ""

        for i in range(a):
            for j in range(b):
                str += '#'
            if i < a - 1:
                str += '\n'
        return str
