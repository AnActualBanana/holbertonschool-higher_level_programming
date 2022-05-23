#!/usr/bin/python3
"""returns the JSON represenation of an object"""


import json


def to_json_string(my_obj):
    """serializes my_obj"""
    my_obj_json = json.dumps(my_obj)
    return my_obj_json
