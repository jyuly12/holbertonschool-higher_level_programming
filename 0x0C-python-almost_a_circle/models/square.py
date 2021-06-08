#!/usr/bin/python3
"""
This module contains Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines the Square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialice a Square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    # Getter and setter

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the Square data"""
        id = self.id
        x = self.x
        y = self.y
        w = self.width

        return "[Square] ({}) {}/{} - {}".format(id, x, y, w)

    def update(self, *args, **kwargs):
        """ defines Update method """
        if args and len(args):
            num = 0
            for i in args:
                if num is 1:
                    self.id = i
                if num is 2:
                    self.size = i
                if num is 3:
                    self.x = i
                if num is 4:
                    self.y = i

        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs[i]
                elif i == "size":
                    self.size = kwargs[i]
                elif i == "x":
                    self.x = kwargs[i]
                elif i == "y":
                    self.y = kwargs[i]

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""

        my_dic = {"id": self.id,
                  "size": self.size,
                  "x": self.x,
                  "y": self.y}
        return my_dic
