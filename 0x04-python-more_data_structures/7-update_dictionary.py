#!/usr/bin/python3

def update_dictionary(a_dictionary: dict, key, value) -> dict:
    """function that replaces or adds key/value in a dictionary

       Args:
           key: the dictionary key
           value: the dictionary value

       Return:
          updated dictionary
    """

    if not a_dictionary:
        return {key: value}

    a_dictionary[key] = value

    return a_dictionary
