#!/usr/bin/python3
"""
defines a rectangle
"""


class Rectangle:
    """ Defines a rectangle by: (based on 7-rectangle.py) """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    """ Height """
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

    """ Returns printable string representation """
    def __str__(self):
        empty_string = ""

        if self.__width == 0 or self.__height == 0:
            return (empty_string)

        r = (((str(self.print_symbol) * self.width) + "\n") * self.height)[:-1]
        return (r)

    """ Returns an official string representation """
    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    """ Print the message  when an instance of Rectangle is deleted """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """ Returns the biggest rectangle considering the area """
    def bigger_or_equal(rect_1, rect_2):

        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return (rect_1)

        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)
