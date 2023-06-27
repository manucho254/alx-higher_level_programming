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

    def __init__(self, size: int = 0, position: tuple = (0, 0)) -> None:
        """ Initializes the instance based on size

            Desc:
                - size must be an integer,
                otherwise raise a TypeError exception,
                with the message size must be an integer.

                - if size is less than 0,
                raise a ValueError exception,
                with the message size must be >= 0.

                - position must be a tuple of 2 positive integers,
                otherwise raise a TypeError exception with the message,
                position must be a tuple of 2 positive integers

            Args:
                size: The size of a square.
                position: square position
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self) -> int:
        """ get the current square area.

            Return:
                  the current square area
        """
        return self.__size * self.__size

    @property
    def size(self) -> int:
        """ getter property, to get current size of square.
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """ setter method to set new values for __size.

            Args:
                new value for __size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self) -> None:
        """ print in stdout the square with the character #

            Desc:
                - if __size == 0 print empty line
                - position should be use by using space,
                - if position[1] > 0 don't fill the lines
        """
        if self.__size == 0:
            print("")
        area = self.area()  # area of the square
        while area != 0:
            if self.__position[1] == 0:
                for i in range(self.__position[0]):
                    print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print("")
            area -= self.__size

    @property
    def position(self) -> tuple:
        """ getter to get position of square
        """
        return self.__position

    @position.setter
    def position(self, value: tuple) -> None:
        """ setter to set new position for square

            Args:
                value: tuple with new position values
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
