#!/usr/bin/python3
"""
This module writen the given names.
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>
    
    Args:
        first_name  (string)
        last_name   (string)
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
