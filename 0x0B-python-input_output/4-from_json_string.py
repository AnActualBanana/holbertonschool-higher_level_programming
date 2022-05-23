#!/usr/bin/python3
"""returns an object represented by a JSON string"""


import json


def from_json_string(my_str):
    """converts JSON string into a dict(python obj) and returns it"""
    my_obj = json.loads(my_str)
    return my_obj
