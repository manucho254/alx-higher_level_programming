#!/usr/bin/python3

def print_list_integer(my_list: list = []) -> None:
    """ function to print all intergers in a list
        Args:
            my_list: a list of integers

        Return:
              None
    """

    for x in reversed(my_list):
        print("{:d}".format(x))
