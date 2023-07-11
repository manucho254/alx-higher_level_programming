#!/usr/bin/python3

""" module that creates an Object from a "JSON file"
"""
import json


def load_from_json_file(filename: str):
    """ create an Object from a "JSON file"
        Args:
            filename: the name of Json file
        Return:
              New json object
    """

    data = {}
    with open(filename, "r") as f:
        file_data = f.read()
        data = json.loads(file_data)

    return data
