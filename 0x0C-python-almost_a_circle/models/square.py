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

    def update(self, *args, **kwargs):
        """ assign arguments to attributes
            Args:
                 args: an array of arguments
                 kwargs: dict ok key word arguments.
            Desc:
                 1st argument should be the id attribute
                 2nd argument should be the size attribute
                 3rd argument should be the x attribute
                 4th argument should be the y attribute
        """
        length_args = len(args)  # length of args

        if length_args > 0:
            for x in range(length_args):
                if x == 0:
                    self.id = args[x]
                if x == 1:
                    self.size = args[x]
                if x == 2:
                    self.x = args[x]
                if x == 3:
                    self.y = args[x]
        else:
            if kwargs.get("id"):
                self.id = kwargs.get("id")
            if kwargs.get("size"):
                self.size = kwargs.get("size")
            if kwargs.get("x"):
                self.x = kwargs.get("x")
            if kwargs.get("y"):
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """ get dictionary representation of Sqaure.
            Return:
                  a dictionary representation of Square.
        """
        new_dict = {'id': self.id, 'x': self.x}
        new_dict.update({'size': self.size, 'y': self.y})

        return new_dict

    def __str__(self):
        """ string representation of Square class.
            Return:
                  string representation of Square class.
        """
        dimension = f"{self.width}"
        position = f"{self.x}/{self.y}"
        message = f"[Square] ({self.id}) {position} - {dimension}"

        return message
