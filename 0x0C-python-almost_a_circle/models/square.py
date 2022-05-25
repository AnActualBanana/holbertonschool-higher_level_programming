#!/usr/bin/python3
"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__x = x
        self.__y = y
        self.__size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, \
                self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
        self.__size = value

    def update(self, *args, **kwargs):
        arg_num = 0
        att_list = ['id', 'size', 'x', 'y']
        for arg in args:
            arg_num += 1
            if arg_num == 1:
                self.id = arg
            elif arg_num == 2:
                self.size = arg
            elif arg_num == 3:
                self.__x = arg
            elif arg_num == 4:
                self.__y = arg
        for key, value in kwargs.items():
            for att in att_list:
                if key == att:
                    setattr(self, key, value)
