#!/usr/bin/python3
"""
This module prints a square
"""


def print_square(size):
    """
    Prints a square with the character #
    
    Arg:
        size (int): square side size.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")

    for hight in range(size):
        for width in range(size):
            print("#", end="")
        print("")
