#!/usr/bin/python3
""" defines a rectangle """


class Rectangle:
    """defines a rectangle by: (based on 4-rectangle.py) """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width """
        return self.__width

    @property
    def height(self):
        """ Height """
        return self.__height

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns rectangle perimiter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ returns printable string representation
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """ return a string representation """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """method called  when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
