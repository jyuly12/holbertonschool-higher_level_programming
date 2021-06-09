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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defines width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Defines height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Defines x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Defines y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the Rectangle area"""
        a = self.__width
        b = self.__height
        return (a * b)

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

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h))

    def update(self, *args, **kwargs):
        """ defines Update method """
        if args and len(args):
            num = 0
            for i in args:
                if num == 1:
                    self.id = i
                if num == 2:
                    self.width = i
                if num == 3:
                    self.height = i
                if num == 4:
                    self.x = i
                if num == 5:
                    self.y = i
            num += 1

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
                   'width': self.width,
                   'height': self.height,
                   'x': self.x,
                   'y': self.y}
        return my_dict
