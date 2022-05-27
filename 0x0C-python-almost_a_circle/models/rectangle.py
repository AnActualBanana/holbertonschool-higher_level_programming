#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiation"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
    """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.__height = value

    @property
    def x(self, value):
        """getter for x"""
        self.__x = value

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self, value):
        """getter for y"""
        self.__y = value

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of model"""
        return(self.width * self.height)

    def display(self):
        """displays the shape of the object"""
        for y_offset in range(0, self.__y):
            print("")
        for lines in range(0, self.__height):
            for x_offset in range(0, self.__x):
                print(" ", end="")
            for hashes in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """returns string representation of object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, \
                self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates attributes of object"""
        arg_num = 0
        att_list = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in args:
                arg_num += 1
                if arg_num == 1:
                    self.id = arg
                elif arg_num == 2:
                    self.width = arg
                elif arg_num == 3:
                    self.height = arg
                elif arg_num == 4:
                    self.x = arg
                elif arg_num == 5:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                for att in att_list:
                    if key == att:
                        setattr(self, key, value)

    def to_dictionary(self):
        """converts object attributes to dictionary"""
        return {'id': self.id, 'width': self.__width, 'height': self.height, \
                'x': self.__x, 'y': self.__y}
