#!/usr/bin/python3

""" module that returns the dictionary description.
"""
import json


def class_to_json(obj):
    """ convert Class to Json
        Args:
            obj: is an instance of a Class
        Reyurn:
             the dictionary description
    """
    return json.dumps(obj.__dict__)
