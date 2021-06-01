#!/usr/bin/python3
"""
This module defines write_file function
"""


def write_file(filename="", text=""):
        """
        writes a string to a text file (UTF8) and returns the number of
        characters.
        """
        with open(filename, 'w', encoding="utf-8") as myfile:
                return myfile.write(text)
