#!/usr/bin/python3

""" module to get all available modules and methods in an object.
"""


def lookup(obj) -> list:
    """ get list of available attributes and methods in object
       Args:
            obj: object to get all attributes and methods.
    """
    return dir(obj)
