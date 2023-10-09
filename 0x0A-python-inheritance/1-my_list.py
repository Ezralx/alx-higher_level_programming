#!/usr/bin/python3

"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort) 
           assuming the elemnts in the list are Type int
        """
        print(sorted(self))
