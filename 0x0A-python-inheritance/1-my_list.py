#!/usr/bin/python3

""" class that inherits from list
"""


class MyList(list):
    """ defines MyList and inherits from list
    """
    def print_sorted(self):
        """ print list sorted in ascending order
        """
        for x in self:
            if not isinstance(x, int):
                print(self)
                break;

        if self is not None:
            print(sorted(self))
