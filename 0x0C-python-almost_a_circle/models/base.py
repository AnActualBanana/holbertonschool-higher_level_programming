#!/usr/bin/python3
"""A base model for all of the other classes in the project."""


class Base:
    """The base object class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """instantiate"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = int(self.__nb_objects)
