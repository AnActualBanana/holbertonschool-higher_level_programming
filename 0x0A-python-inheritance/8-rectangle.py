#!/usr/bin/python3
"""A Rectangle class, that inherits from BaseGeometry, that's instantiated with\
 width and height"""

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

class Rectangle(BaseGeometry):
    """The Rectangle class"""
    def __init__(self, width, height):
        """instantiation checks for valid width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
