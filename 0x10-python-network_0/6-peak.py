#!/usr/bin/python3
""" module to find peak in a list
"""


def find_peak(list_of_integers: list) -> int:
    """ find peak in a list
        Args:
            list_of_integers: an array of lists
    """
    # base case
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    length = len(list_of_integers)
    peak = None

    for x in range(length - 1):
        if list_of_integers[x] >= list_of_integers[x - 1]\
                and list_of_integers[x] >= list_of_integers[x + 1]:
            peak = list_of_integers[x]
            break

    return peak
