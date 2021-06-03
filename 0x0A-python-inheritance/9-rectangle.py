#!/usr/bin/python3
"""
This module defines a Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        a = self.__width
        b = self.__height
        return a * b

    def __str__(self):
        a = self.__width
        b = self.__height
        return (f"[Rectangle] {a}/{b}")
