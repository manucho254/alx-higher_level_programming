#!/usr/bin/python3

""" MagicClass Turn Opcodes to the class below
"""
import math
import dis


class MagicClass:
    """ defines a class to calcute

        Attributes:
                  __radius: radius of a circle.
    """
    def __init__(self, radius):
        """ Initialize MagicClass.

            Args:
                 radius: radius of a circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self, radius):
        """ get area of a circle:

            Args:
                radius: radius of a circle
            Return:
                area of a circle
        """
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """ get circumfrence of a circle

            Args:
                radius: radius of a circle.
            Return:
                circumference of a circle
        """
        return 2 * math.pi * self.__radius


dis.dis(MagicClass)
