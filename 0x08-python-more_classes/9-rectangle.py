#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    creates a class

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle class
        Args:

            width (int): size of the Rectangle.

            height (int): size of the Rectangle.
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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
        return (2 * (a + b))

    def __str__(self):
        """
        generate a printeable rectangle
        """
        a = self.__height
        b = self.__width

        if a is 0 or b is 0:
            return ""

        str_print = ""

        for i in range(a):
            for j in range(b):
                str_print += str(self.print_symbol)
            if i < a - 1:
                str_print += '\n'
        return str_print

    def __repr__(self):
        """
        generate a string representation of rectangle
        """
        a = self.__width
        b = self.__height
        return "Rectangle(" + str(a) + ", " + str(b) + ")"

    def __del__(self):
        """
        print a message than delete rectangle class
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Obtain the biggest rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """
        creates a new rectangle instance
        """
        return cls(size, size)
