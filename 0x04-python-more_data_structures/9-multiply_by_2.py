#!/usr/bin/python3

def multiply_by_2(a_dictionary: dict) -> dict:
    """ function that returns a new dictionary with,
        all values multiplied by 2

        Args:
            a_dictionary: a dictionary

        Return:
             returns a new dictionary with all values multiplied by 2
   """

    if a_dictionary is None:
        return {}

    return {x: (a_dictionary[x] * 2) for x in a_dictionary}
