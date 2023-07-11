#!/usr/bin/python3

""" module to write an Object to a file using Json representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ write an Object to a file using Json representation
        Args:
            my_obj: object to write to file as Json.
            filename: name of file to write data to.
    """
    with open(filename, "w") as f:
        load_obj = json.dumps(my_obj)
        f.write(str(load_obj))
