#!/usr/bin/python3

""" module that inserts a line of text to a file,
    after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """ insert a line of text to a file,
        after each line containing a specific string
        Args:
            filename: name of file to append text to.
            seach_string: string to look for in file.
            new_string: new string to add to file after finding search string
    """
    data = []

    with open(filename, "r") as f:
        data = f.readlines()

    """ loop through array adding new string text
        if search string is found
    """
    length = len(data)

    if length == 0:
        return

    for x in range(length - 1):
        if search_string in data[x]:
            if x != length - 1:
                data.insert(x + 1, new_string)

    with open(filename, "w") as f:
        f.write("".join(data))
