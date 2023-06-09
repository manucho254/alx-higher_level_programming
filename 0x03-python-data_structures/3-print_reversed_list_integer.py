#!/usr/bin/python3

def print_reversed_list_integer(my_list: list = []) -> None:
    """ function to print all intergers in a list in reverse
        Args:
            my_list: a list of integers

        Return:
              None
    """

    length = len(my_list)
    for x in range(length, 0, -1):
        print("{0:d}".format(x))
