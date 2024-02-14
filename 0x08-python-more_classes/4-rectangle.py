#!/usr/bin/python3
"""
defines a rectangle
"""


class Rectangle:
    """ Defines a rectangle by: (based on 3-rectangle.py) """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Width """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Hight """
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Rectangle area """
    def area(self):
        return (self.__height * self.__width)

    """ Rectangle perimeter """
    def perimeter(self):
        if self.width == 0:
            return (0)
        if self.height == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    """ Returns  string representation """
    def __str__(self):
        empty_string = ""

        if self.__width == 0 or self.__height == 0:
            return (empty_string)

        return ((('#' * self.width) + "\n") * self.height)[:-1]

    """ Returns an official string representation """
    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
