#!/usr/bin/python3

""" module to check if object is a subclass of a specified class
"""


def is_kind_of_class(obj, a_class) -> bool:
    """ check if object is a subclass of specified class
        Args:
            obj: object to check if subclass
            a_class: class object
        Return:
              True if obj is a subclass of a_class else return False
    """
    return issubclass(type(obj), a_class)
