#!/usr/bin/python3

def add_tuple(tuple_a: tuple = (), tuple_b: tuple = ()) -> tuple:
    """ function that adds the values of two tuples
        Args:
            tuple_a: a tuple of integers
            tuple_b: a tuple of integers

        Return:
            a tuple with the sum of values from tuple_a and tuple_b
    """
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    len_a = len(list_a)
    len_b = len(list_b)

    if len_a > 2:
        list_a = list_a[0:2]
    if len_b > 2:
        list_b = list_b[0:2]

    list_a = add_zero_to_list(list_a, len_a)
    list_b = add_zero_to_list(list_b, len_b)

    value_a = list_a[0] + list_b[0]
    value_b = list_a[1] + list_b[1]

    return (value_a, value_b)


def add_zero_to_list(my_list: list, length: int) -> list:
    """ function that adds 0 to a list if certain conditions are met.

        Args:
           my_list: a list of integers
           length: the length of the list

        Return:
              my_list modified or just the same
    """
    if length == 0:
        my_list.append(0)
        my_list.append(0)

    if length == 1:
        my_list.append(0)

    return my_list
