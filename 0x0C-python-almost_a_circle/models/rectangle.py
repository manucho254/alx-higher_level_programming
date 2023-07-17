#!/usr/bin/python3

""" class Rectangle that inherits from base.
"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize class Rectangle
            Args:
                 width: width of a rectangle
                 height: height of a rectangle
                 x: xaxis position
                 y: yaxis position
                 id: Object id
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError(f"width must be an integer")
        if width < 1:
            raise ValueError(f"width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError(f"height must be an integer")
        if height < 1:
             raise ValueError(f"height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError(f"x must be an integer")
        if x < 0:
            raise ValueError(f"x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError(f"y must be an integer")
        if y < 0:
            raise ValueError(f"y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """ get the width of the rectangle.
            Return:
                  width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ update the width of the rectangle
            Args:
                width: new rectangle width
        """
        if not isinstance(width, int):
            raise TypeError(f"width must be an integer")
        if width < 1:
            raise ValueError(f"width must be > 0")

        self.__width = width

    @property
    def height(self):
        """ get the height of the rectangle
            Return:
                   height of the rectangle
        """
        
        return self.__height

    @height.setter
    def height(self, height):
        """ update the height of a rectangle.
            Args:
                height: height of a rectangle
        """
        if not isinstance(height, int):
            raise TypeError(f"height must be an integer")
        if height < 1:
            raise ValueError(f"height must be > 0")

        self.__height = height

    @property
    def x(self):
        """ get the value of x
            Return:
                  xaxis position.
        """
        return self.__x

    @x.setter
    def x(self, x=0):
        """ update x value
            Args:
                x: new xaxis value of rectangle
        """
        if not isinstance(x, int):
            raise TypeError(f"x must be an integer")
        if x < 0:
            raise ValueError(f"x must be >= 0")

        self.__x = x

    @property
    def y(self):
        """ get value of y
            Return:
                  yaxis position
        """

        return self.__y

    @y.setter
    def y(self, y=0):
        """ update y value
            Args:
                y: new yaxis value of rectangle
        """
        if not isinstance(y, int):
            raise TypeError(f"y must be an integer")
        if y < 0:
            raise ValueError(f"y must be >= 0")

        self.__y = y
