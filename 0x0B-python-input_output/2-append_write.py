#!/usr/bin/python3

""" module to append to a text file
"""


def append_write(filename: str = "", text: str = "") -> int:
    """ append data to a file and return numbers of characters written
        Args:
            filename: file to read data.
            text: new text to write to file.
        Return:
             number of characters written.
    """

    length = 0
    with open(filename, "a") as f:
        length = f.write(text)

    return length
