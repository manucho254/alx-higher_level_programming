#!/usr/bin/python3

""" module to return json representation of an object
"""
import json


def from_json_string(my_str: str):
    """ convert object to string
        Args:
            my_obj: object data
        Return:
              json representation of my_obj
    """
    return json.loads(my_str)
