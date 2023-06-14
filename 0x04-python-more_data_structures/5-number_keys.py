#!/usr/bin/python3

def number_keys(a_dictionary: dict) -> int:
    """function that returns the number of keys in a dictionary

       Args:
           a_dictionary: a dictionary

       Return:
           number of keys
    """

    if a_dictionary:
        return len(a_dictionary.keys())

    return 0
