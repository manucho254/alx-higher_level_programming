#!/usr/bin/python3

def element_at(my_list: list, idx: int) -> int:
    """ function to get element at specified index

        Args:
            my_list: an array of integers
            idx: index to find item

        Returns:
            the integer at idx and if fails returns None

    """
    length = len(my_list) - 1

    if idx < 0 or idx > length:
        return None

    return my_list[idx]
