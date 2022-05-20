#!/usr/bin/python3
"""a student class that has name, age, and a method to retrieve\
a dictionary representation of a Stduent instance"""


class Student:
    """class with name and age, and a method that returns a dict\
representation of itself"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
