#!/usr/bin/python3

def print_reversed_list_integer(my_list: list = []) -> None:
    """ function to print all intergers in a list in reverse

        Args:
            my_list: a list of integers

        Return:
              None
    """

    if my_list:
        for x in reversed(my_list):
            print("{:d}".format(x))
