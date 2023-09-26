#!/usr/bin/python3
""" a class  that defines square"""


class Square:
    """ defines property of a square"""

    def __init__(self, size=0):
        """ creates instance of a square
        Args:
            size (int): size of one side of a square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square

    def area(self):
        """returns the area.

        Returns:
            ares.
        """
        return self.__size ** 2
