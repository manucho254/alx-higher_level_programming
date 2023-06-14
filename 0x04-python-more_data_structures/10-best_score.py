#!/usr/bin/python3

def best_score(a_dictionary: dict):
    """ function that returns a key,
        with the biggest integer value

        Args:
            a_dictionary: a dictionary

        Return:
              key with biggest integer else return None
    """

    if a_dictionary:
        max_val = max(a_dictionary.values())
        for x in a_dictionary:
            if a_dictionary[x] == max_val:
                return x

    return None
