#!/usr/bin/python3
"""a student class that has name, age, and a method to retrieve\
a dictionary representation of a Stduent instance"""


class Student:
    """class with name and age, and a method that returns a dict\
representation of itself"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict representation of attributes specified,\
 or all attributes if none are specified"""
        if attrs is not None:
            old_dict = self.__dict__
            new_dict = dict()
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
                for key in [*old_dict]:
                    if key == attr:
                        new_dict[key] = old_dict[key]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        old_dict = self.__dict__
        for (key, value) in json.items():
            setattr(self, key, value)
