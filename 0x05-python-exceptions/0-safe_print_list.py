#!/usr/bin/python3

def safe_print_list(my_list: list = [], x: int = 0):
    """ safe_print_list - function that prints x elements of a list.

        Args:
            my_list: a list of differnt elements
            x: number of elements to print.

        Return:
            the number of elements printed.
    """
    printed_items_count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_items_count += 1
    except Exception as e:
        pass

    print()
    return printed_items_count
