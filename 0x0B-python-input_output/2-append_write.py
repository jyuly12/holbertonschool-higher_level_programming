#!/usr/bin/python3
"""
This module defines append_file function
"""


def append_file(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as myfile:
        return myfile.write(text)
