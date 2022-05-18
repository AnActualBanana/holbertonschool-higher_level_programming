#!/usr/bin/python3
"""function check if obj is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """returns True is object is exactly instance of class, false otherwise"""
    if type(obj) == a_class:
        return True
    if type(obj) != a_class:
        return False
