#!/usr/bin/python3

def update_dictionary(a_dictionary: dict, key, value):
    """function that replaces or adds key/value in a dictionary

       Args:
           key: the dictionary key
           value: the dictionary value

       Return:
          updated dictionary
    """

    if a_dictionary:
        if key:
            a_dictionary[key] = value
        return a_dictionary

    return {}
