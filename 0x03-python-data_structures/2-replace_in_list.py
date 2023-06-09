#!/usr/bin/python3

def replace_in_list(my_list: list, idx: int, element: int) -> list:
    """ function to replace element in list

        Args:
            my_list: an array of integers
            idx: index to find item
            element: new item to add in list at index idx

        Returns:
            a list of integers

    """
    length = len(my_list) - 1

    if idx < 0 or idx > length:
        return my_list

    del my_list[idx]
    my_list.insert(idx, element)

    return my_list
