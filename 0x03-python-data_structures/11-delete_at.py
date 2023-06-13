#!/usr/bin/python3

def delete_at(my_list: list = [], idx: int = 0) -> list:
    """ function that deletes an item at specific index

        Args:
            my_list: array to delete item from
            idx: index to find item

        Return:
             list without item at index idx else,
             return just my_list
    """

    length = len(my_list) - 1

    if length == 0:
        return my_list

    if idx < 0 or idx > length:
        return my_list

    del my_list[idx]

    return my_list
