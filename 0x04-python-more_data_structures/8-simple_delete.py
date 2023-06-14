#!/usr/bin/python3

def simple_delete(a_dictionary: dict, key: str = ""):
    """ function that deletes a key in a dictionary.

        Args:
            key: key to find in dictionary

        Return:
              dictionary with one element deleted
    """

    if not a_dictionary:
        return a_dictionary

    if not a_dictionary.get(key):
        return a_dictionary

    del a_dictionary[key]

    return a_dictionary
