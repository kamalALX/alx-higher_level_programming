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
        if len(value) not 2 or value[0] < 0 or value[1] < 0
        or not isinstance(value, tuple)
        or not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        slef.__position = position

    def area(self):
        """ returns the current square area """
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                for k in range(self.position[0]):
                    print(" "end="")
                print()
