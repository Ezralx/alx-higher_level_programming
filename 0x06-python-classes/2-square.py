#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    a Class that defines square

    """
    def __init__(self, size=0):
        """Creates attribute or new instance for  square.

        Args:
            size (int): one side of the square
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
