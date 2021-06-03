#!/usr/bin/python3
"""
This module defines the square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        a = self.__size
        return a ** 2

    def __str__(self):
        a = self.__size
        return (f"[Square] {a}/{a}")
