#!/usr/bin/python3

""" module that returns the dictionary description.
"""


def class_to_json(obj):
    """ convert Class to Json
        Args:
            obj: is an instance of a Class
        Reyurn:
             the dictionary description
    """
    return obj.__dict__
