#!/usr/bin/python3

def safe_print_list_integers(my_list: list = [], x: int = 0):
    """ safe_print_list_integers - function that prints x,
        elements of a list and only integers.

        Args:
            my_list: a list of differnt elements
            x: number of elements to print.

        Return:
            the number of elements printed.
    """
    printed_items_count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                printed_items_count += 1
    except Exception as e:
        raise e

    print()
    return printed_items_count
