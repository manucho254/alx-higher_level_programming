#!/usr/bin/python3

""" function that prints a square with the character #
"""


def print_square(size):
    """ print a square with the character #
        Args:
            size: the dimension of a square
    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
