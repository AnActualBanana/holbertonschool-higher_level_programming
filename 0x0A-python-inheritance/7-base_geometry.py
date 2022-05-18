#!/usr/bin/python3
"""class with a public instance method that's not currently implemented\
, as well as a method that validates an int as a positive int."""


class BaseGeometry:
    """class"""
    def area(self):
        """not currently implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """checks if value is an int, and if its positive"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
