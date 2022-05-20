#!/usr/bin/python3
"""creates an object from a JSON file"""


import json

def load_from_json_file(filename):
    """creates an object from a JSON file"""
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        my_obj = json.loads(read_data)
        return my_obj
