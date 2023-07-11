#!/usr/bin/python3

""" script that adds all arguments to a Python list, and then save them to a file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_to_file():
    """ add all command line arguments to python list
        Return:
              the list data
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
        with open(filename, 'r') as f:

            data = json.loads(f.read().strip("\n"))
            data.extend(arr)

        save_to_json_file(data, filename)

    except FileNotFoundError as e:
        with open(filename, 'w') as f:
            f.write(json.dumps(arr))
        data = load_from_json_file(filename)

    return data


if __name__ == "__main__":
    add_to_file()
