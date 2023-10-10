#!/usr/bin/python3
"""
    The 5-test_indentation module.

"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new line

    Args:
        text (str): string to be examined.

    Raises:
        TypeError: If text is not of type str.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
