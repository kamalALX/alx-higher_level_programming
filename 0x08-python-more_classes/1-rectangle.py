#!/usr/bin/python3
""" an empty class Rectangle that defines a rectangle """


class Rectangle:
    """ a class that defines a rectangle """
    def __init__(self, width=0, height=0):
        """ Initializes a new Rectangle.
        Args:
            width(int): represents the width of the new rectangle
            height(int): represents the height of the new rectangle
        """

        self.height = height
        self.width = width

    @property
    def width():
        return slef.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height():
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
