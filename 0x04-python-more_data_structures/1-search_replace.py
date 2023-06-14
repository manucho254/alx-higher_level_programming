#!/usr/bin/python3

def search_replace(my_list: list, search: int, replace: int) -> list:
    """function that replaces all occurrences,
       of an element by another in a new list

       Args:
           my_list: list of integers
           search: element to search in list
           replace: element to replace search in new list

       Return:
           new list with element search replaced with replace

    """

    if len(my_list) == 0:
        return my_list

    new = list(map(lambda x: replace if x == search else x, my_list))

    return new
