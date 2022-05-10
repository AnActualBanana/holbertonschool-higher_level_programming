#!/usr/bin/python3
"a class that defines a square"

class Square:
    "defines a square with size, instantiation, and public instance method"
    def __init__(self, size=0):
        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return(self.__size * self.__size)
