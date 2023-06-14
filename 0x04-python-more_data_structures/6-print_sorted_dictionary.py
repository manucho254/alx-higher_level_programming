#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary: dict) -> None:
    """ function that prints a dictionary by ordered keys
        Args:
            a_dictionary: a dictionary of different datatypes

        Return:
              None
    """
    if a_dictionary:
        for x in sorted(a_dictionary):
            print("{}: {}".format(x, a_dictionary[x]))
