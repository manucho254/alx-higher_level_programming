#!/usr/bin/python3
""" Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class defines a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize class Square
            Args:
                size: size of the square
                x: xaxis position of square
                y: yaxis position of square
                id: id of object
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    @property
    def size(self):
        """ get size of a square.
            Return:
                  the size of a square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """ update the size of a square.
            Args:
                size: new size of a square.
        """
        self.width = size
        self.height = size

    def __str__(self):
        """ string representation of Square class.
            Return:
                  string representation of Square class.
        """
        dimension = f"{self.width}"
        position = f"{self.x}/{self.y}"
        message = f"[Square] ({self.id}) {position} - {dimension}"

        return message
