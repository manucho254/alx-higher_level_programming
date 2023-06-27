#!/usr/bin/python3

def list_division(my_list_1: list, my_list_2: list, list_length: int):
    """ list_division - function that divides element by element 2 lists.

        Args:
            my_list_1: list 1 of different elements
            my_list_2: list 2 of different elements

        Return:
            Return new list (length = list_length) with all divisions.
    """
    res = 0
    new_list = []
    types = (float, int)

    if len(my_list_1) == 0:
        for i in range(list_length):
            new_list.append(0)
        return new_list

    if len(my_list_2) == 0:
        for j in range(list_length):
            new_list.append(0)
        return new_list

    try:
        for x in range(list_length):
            a, b = my_list_1[x], my_list_2[x]
            if not isinstance(a, types) or not isinstance(b, types):
                print("wrong type")
                new_list.append(0)
                continue
            if b == 0:
                print("division by 0")
                new_list.append(0)
                continue
            res = a / b
            new_list.append(res)
    except Exception as e:
        if isinstance(e, IndexError):
            print("out of range")
            new_list.append(0)
    finally:
        return new_list
