#!/usr/bin/python3

"""class Square that defines a square """


class Square:
    """ Represent a square, with size."""

    def __init__(self, size=0):
        """ Initializes a new square.
        Args:
            size (int): represents the size of the nez square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an intiger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
