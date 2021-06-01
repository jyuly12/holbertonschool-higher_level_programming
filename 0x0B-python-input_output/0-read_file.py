#!/usr/bin/python3
"""
This module defines read_file function.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
