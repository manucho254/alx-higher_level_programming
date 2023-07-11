#!/usr/bin/python3

""" module to add new attribute to class
"""


def add_attribute(obj, name, value):
    """ add new attribute to class
        Args:
            obj: Class to add new attribute
            name: name of new attribute
            value: value for new class attribute
    """
    modules = dir(obj)

    if "__dict__" in modules:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
