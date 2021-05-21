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
        return self.__width

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
