#!/usr/bin/python3
"""
This module defines load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”
    """
    with open(filename) as myfile:
        return json.load(myfile)
