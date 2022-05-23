#!/usr/bin/python3
"""writes an object to a text file, using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file in JSON"""
    my_obj_json = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(my_obj_json)
