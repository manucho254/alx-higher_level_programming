#!/usr/bin/python3

"""class Square that defines a square

   Attributes:
            __size: Private instance attribute
"""


class Square:
    """class Square that defines a square.

       Attributes:
            __size: Private instance attribute
    """

    def __init__(self, size: int = 0) -> None:
        """ Initializes the instance based on size

            Desc:
                size must be an integer,
                otherwise raise a TypeError exception,
                with the message size must be an integer.

                if size is less than 0,
                raise a ValueError exception,
                with the message size must be >= 0.

            Args:
                size: The size of a square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
