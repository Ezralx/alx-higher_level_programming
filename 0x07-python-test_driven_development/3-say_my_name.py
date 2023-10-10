#!/usr/bin/python3
"""
    The say_my_name module
"""


def say_my_name(first_name, last_name=""):
    """
        prints my name <first name> <last name>.

        Args:
        first_name:must be strings
        last_name: must be a string
    """
    if first_name == "" and last_name == "":
        return None
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
