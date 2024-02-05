#!/usr/bin/python3
""" a module that contain a class called BaseGeometry. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class the represents a square """
    def __init__(self, size):
        """ initialization method """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns the area of a square """
        return self.__size ** 2

    def __str__(self):
        """ String representation of the class """
        return ("[Square] " + str(self.size) + "/" + str(self.size))
