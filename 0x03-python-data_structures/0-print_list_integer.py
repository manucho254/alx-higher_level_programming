#!/usr/bin/python3

def print_list_integer(my_list: list = []) -> None:
    """ function to print all intergers in a list
        Args:
            my_list: a list of integers

        Return:
              None
    """

    new = reversed(my_list)
    for x in new:
        print("{:d}".format(x))
