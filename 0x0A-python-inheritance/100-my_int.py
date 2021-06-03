#!/usr/bin/python3
"""
This module contains the MyInt class
"""


class MyInt(int):
    """
    Defines a MyInt class
    """
    def __eq__(self, other_int):
        return int.__ne__(self, other_int)

    def __ne__(self, other_int):
        return int.__eq__(self, other_int)
