#!/usr/bin/python3
"""
This module defines a lookup function.
"""


def lookup(obj):
    """
    Returns the list of available attributes and
    of an object
    """
    return dir(obj)
