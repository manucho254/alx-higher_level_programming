#!/usr/bin/python3

""" module to write to a text file
"""


def write_file(filename: str = "", text: str = "") -> int:
    """ write date to a file and return numbers of characters written
        Args:
            filename: file to read data.
            text: new text to write to file.
        Return:
             number of characters written.
    """

    length = 0
    with open(filename, "w") as f:
        length = f.write(text)

    return length
