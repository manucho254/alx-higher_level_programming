#!/usr/bin/python3

""" class that inherits from list
"""


class MyList(list):
    """ defines MyList and inherits from list
    """
    def print_sorted(self):
        """ print list sorted in ascending order
        """

        if self is None:
            return

        if any(not isinstance(x, int) for x in self):
            print(self)
            return

        print(sorted(self))
