#!/usr/bin/python3
"""checks if the object is an instance of or instance of subclass of specified \
class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of or is an instance of class\
that inherited from, the specified class, otherwise returns False"""
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
