#!/usr/bin/python3
"""
This module defines append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string.

    Args:
        filename (str)
        search_string (str)
        new_string (str)
    """
    new = ""
    with open(filename, 'r') as read_file:
        for line in read_file:
            new += line
            if search_string in line:
                new.append(new_string)

    with open(filename, "w") as f:
        f.write(new)
