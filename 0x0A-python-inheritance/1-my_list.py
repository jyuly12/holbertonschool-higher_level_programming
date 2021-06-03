#!/usr/bin/python3
"""
This module defines MyList class
"""


class MyList(list):
    """
    Prints the list, but sorted (ascending sort)
    """
    def print_sorted(self):
        print(sorted(self))
