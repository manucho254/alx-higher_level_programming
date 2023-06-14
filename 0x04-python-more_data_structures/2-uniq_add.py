#!/usr/bin/python3

def uniq_add(my_list: list = []) -> int:
    """function that adds all unique integers ,
       in a list (only once for each integer)

       Args:
           my_list: an array of integers

       Return:
             the sum of unique integer
    """

    if len(my_list) == 0:
        return 0

    new = []

    for x in my_list:
        if x not in new:
            new.append(x)

    return sum(new)
