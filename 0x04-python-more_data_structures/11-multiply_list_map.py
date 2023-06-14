#!/usr/bin/python3

def multiply_list_map(my_list: list = [], number: int = 0) -> list:
    """ function that returns a list with all values,
        multiplied by a number without using any loops.

        Args:
            my_list: a list of integers
            number: mutiply by this number

        Return:
             a new list with all element multiplied by number
    """

    if len(my_list) == 0:
        return []

    return list(map(lambda x: x * number, my_list))
