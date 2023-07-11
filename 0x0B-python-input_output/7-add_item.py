#!/usr/bin/python3

""" script that adds all arguments to a Python list, and then save them to a file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_to_file():
    """ add all command line arguments to python list
    """
    args = sys.argv
    arr = []  # initialize array
    filename = "add_item.json"
    num_args = len(args)

    # check for arguments
    if num_args > 1:
        for x in range(1, num_args):
            arr.append(args[x])

    try:
        data = load_from_json_file(filename)
        data.extend(arr)
        save_to_json_file(data, filename)
    except Exception as e:
        with open(filename, 'w') as f:
            f.write(json.dumps(arr))


if __name__ == "__main__":
    add_to_file()
