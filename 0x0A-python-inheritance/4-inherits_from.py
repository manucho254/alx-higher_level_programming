#!/usr/bin/python3

""" module to check if the object is an instance of a class,
    that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class) -> bool:
    """ check if object is a subclass of specified class and instance
        Args:
            obj: object to check if subclass and instance
            a_class: class object
        Return:
              True if obj is a subclass and,
              instance of a_class else return False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
