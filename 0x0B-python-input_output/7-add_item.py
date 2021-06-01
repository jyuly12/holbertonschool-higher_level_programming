#!/usr/bin/python3
"""
This module adds all arguments to a Python list, and then save them to a file.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
data = []

with open(file_name, "a") as myfile:
    if myfile.tell() == 0 and len(sys.argv) == 1:
            myfile.write("[]")

    elif len(sys.argv) > 1:
        data = load_from_json_file(file_name)
        data.extend(sys.argv[1:])
        save_to_json_file(data, file_name)
