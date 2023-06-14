#!/usr/bin/pytjon3

def common_elements(set_1: set, set_2: set) -> set:
    """ function that returns a set of common,
        elements in two sets

        Args:
            set_1: a set of strings
            set_2: a set of strings

        Return:
             a set of common values in set_1 and set_2
    """
    if len(set_1) == 0 and len(set_2) == 0:
        return set()

    return {x for x in set_1 if x in set_2}
