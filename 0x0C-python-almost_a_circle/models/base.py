#!/usr/bin/python3
"""A base model for all of the other classes in the project."""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """creates JSON representation of object"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """saves JSON representation of object to file."""
        clsfile = cls.__name__ + ".json"
        with open(clsfile, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))
