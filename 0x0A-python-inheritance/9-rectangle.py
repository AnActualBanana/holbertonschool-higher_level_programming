#!/usr/bin/python3
"""A Rectangle class, that inherits from BaseGeometry, that's instantiated \
 wwith width and height"""


class BaseGeometry:
    """class for geometry"""
    def area(self):
        """gets the area of the geometry"""
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

    def area(self):
        self.__area = self.__width * self.__height
        return self.__area

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __repr__(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))
