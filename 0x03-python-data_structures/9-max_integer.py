#!/usr/bin/python3

def max_integer(my_list: list = []):
    """ function to get maximum value in list

        Args:
            my_list: string to find the max value

        Return:
              None if list is empty else return max value

    """
    max_val = None

    for x in my_list:
        max_val = x
        for k in my_list:
            if k > max_val:
                max_val = k

    return max_val
