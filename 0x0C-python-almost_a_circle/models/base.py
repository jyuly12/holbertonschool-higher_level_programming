#!/usr/bin/python3
"""
This module contains the base class
"""
import json
import os.path


class Base:
    """
    Creates de Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base class.

        Args:
        id (int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        lists = []
        if list_objs is not None:
            for i in list_objs:
                lists.append(cls.to_dictionary(i))
        with open(filename, 'w') as files:
            files.write(cls.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        lists = []
        if json_string is None or len(json_string) == 0:
            return lists
        else:
            lists = json.loads(json_string)
            return lists

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dic = cls(1, 1)
            else:
                dic = cls(1)
            new.update(**dictionary)
            return dic

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = "{}.json".format(cls.__name__)
        lists = []
        if os.path.isfile(file_name):
            with open(file_name, "r") as my_file:
                lists = cls.from_json_string(my_file.read())

            for i in range(0, len(lists)):
                lists[i] = cls.create(**lists[i])
        return lists
