#!/usr/bin/python3

def copy_list(my_list: list = []) -> list:
    """ function to copy data from one list to another

       Args:
           my_list: a list of integers

       Return:
             a list of integers

    """

    return [x for x in my_list]


def new_in_list(my_list: list, idx: int, element: int) -> list:
    """ function to replace element in list

        Args:
            my_list: an array of integers
            idx: index to find item
            element: new item to add in list at index idx

        Returns:
            a copy of my_list

    """
    length = len(my_list) - 1

    if idx < 0 or idx > length:
        return copy_list(my_list)

    new_list = copy_list(my_list)
    # delete and insert at index idx
    del new_list[idx]
    new_list.insert(idx, element)

    return new_list
