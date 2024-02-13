#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    """Represents a rectangle by: (based on 0-rectangle.py)"""

    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Width """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    """ Height """
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
