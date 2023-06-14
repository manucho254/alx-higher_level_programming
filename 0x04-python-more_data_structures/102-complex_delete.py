#!/usr/bin/python3

def complex_delete(a_dictionary: dict, value) -> dict:
    """function that deletes keys with a,
       specific value in a dictionary

       Args:
           a_dictionary: a python dictionary
           value: value to delete from dictionary
    """

    if a_dictionary is None:  # check if dictionary is None
        return a_dictionary

    if value not in a_dictionary.values():
        return a_dictionary

    items = list(a_dictionary.items())  # all items in dictionary
    for x, y in items:
        if y == value:
            del a_dictionary[x]

    return a_dictionary
