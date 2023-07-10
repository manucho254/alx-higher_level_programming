#!/usr/bin/python3

""" module to check if object is an instance of specified class
"""


def is_same_class(obj, a_class) -> bool:
    """ check if object is an instance of specified class
        Args:
            obj: object to check if instance of a_class
            a_class: class object
        Return:
               True if instance of class else false
    """
    return isinstance(obj, a_class) and type(obj) == a_class
