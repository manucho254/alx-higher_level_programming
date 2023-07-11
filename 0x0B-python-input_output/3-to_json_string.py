#!/usr/bin/python3

""" module to return json representation of an object
"""
import json


def to_json_string(my_obj):
    """ convert object to string
        Args:
            my_obj: object data
        Return:
              json representation of my_obj
    """
    return json.dumps(my_obj)
