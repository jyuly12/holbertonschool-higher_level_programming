#!/usr/bin/python3
"""
This module defines the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialice the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

# Getters and setters of all arguments

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

# ___PUBLIC__METHODS___

    def area(self):
        """Returns the Rectangle area"""
        a = self.__width
        b = self.__height
        return a * b

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.width == 0 or self.height == 0:
            print("")
        else:
            for y in range(self.y):
                print("")
            for i in range(self.height):
                for j in range(self.x):
                    print(" ", end="")
                for k in range(self.width):
                    print("#", end="")
                print("")

    def __str__(self):
        """ This method returns rectangle data"""

        id = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height

        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def update(self, *args, **kwargs):
        """ defines Update method """
        if args and len(args):
            num = 0
            for i in args:
                if num is 1:
                    self.id = i
                if num is 2:
                    self.width = i
                if num is 3:
                    self.height = i
                if num is 4:
                    self.x = i
                if num is 5:
                    self.y = i
        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]

                elif i == "width":
                    self.width = kwargs[i]

                elif i == "height":
                    self.height = kwargs[i]

                elif i == "x":
                    self.x = kwargs[i]

                elif i == "y":
                    self.y = kwargs[i]

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""

        my_dict = {'id': self.id,
                   'width': self.width
                   'height': self.height,
                   'x': self.x,
                   'y': self.y}
        return my_dict
