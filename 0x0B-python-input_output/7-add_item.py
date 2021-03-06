#!/usr/bin/python3
"""
This module adds all arguments to a Python list, and then save them to a file.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

try:
    new_data = load_from_json_file(filename)
except:
    new_data = []

for i in sys.argv[1:]:
    new_data.append(i)

save_to_json_file(new_data, file_name)
