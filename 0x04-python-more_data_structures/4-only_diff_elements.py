#!/usr/bin/python3

def only_diff_elements(set_1: set, set_2: set) -> set:
    """ function that returns a set of all ,
        elements present in only one set.

        Args:
            set_1: a set of strings
            set_2: a set of strings

        Return:
             a set of elements present in only one set
    """
    if len(set_1) == 0 and len(set_2) == 0:
        return set()

    arr_1 = [x for x in set_1 if x not in set_2]
    arr_2 = [i for i in set_2 if i not in set_1]

    return set(arr_1 + arr_2)
