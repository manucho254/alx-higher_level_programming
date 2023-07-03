#!/usr/bin/python3

""" class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class Rectangle
        Attributes:
                  width: the width of the rectangle
                  height: height of rectangle
    """
    def __init__(self, width=0, height=0):
        """ initialize class
            Args:
                width: width of a rectangle
                height: height of a rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter to get width of a rectangle
            Return:
                   width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter to set new width of a rectangle
            Args:
                value: new width ofa rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter to get height of a rectangle
            Return:
                   height of a rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter to set new height of a rectangle
            Args:
                value: new height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ get area of a rectangle
            Return:
                   the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ get perimeter of a rectangle
            Return:
                   the perimeter of a rectangle
        """
        return (self.__height * 2) + (self.__width * 2)
