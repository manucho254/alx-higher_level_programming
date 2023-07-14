#!/usr/bin/python3

""" Base class
"""


class Base:
    """ base class for all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize the base class
            Args:
                id: integer value
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
