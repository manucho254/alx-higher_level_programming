#!/usr/bin/python3

""" module to read a text file
"""


def read_file(filename: str = "") -> None:
    """ read file and print the text
        Args:
            filename: file to read data
    """
    with open(filename, "r") as f:
        print(f.read(), end="")
