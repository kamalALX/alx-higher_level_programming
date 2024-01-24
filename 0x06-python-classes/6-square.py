#!/usr/bin/python3

"""class Square that defines a square """


class Square:
    """ Represent a square, with size."""

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a new square.
        Args:
            size (int): represents the size of the nez square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the current square area """
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
