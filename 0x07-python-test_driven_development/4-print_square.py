#!/usr/bin/python3
"""
    The print_square module.
"""


def print_square(size):
    """ prints a square using '#' based on `size`.

    Args:
        size (int): The length of one side of the square.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(('#' * size + '\n') * size, end='')
