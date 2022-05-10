#!/usr/bin/python3
"A class that defines a square"

class Square:
    "the square class, containing size and instantiation"
    def __init__(self, size=0):
        if isinstance(size, int) != True:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
