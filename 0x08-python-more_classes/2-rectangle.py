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
        self.width = width
        self.height = height

    @property
    def width():
        return slef.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height():
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ returns the rectangle perimeter """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the rectangle perimeter """

        pmeter = 2 * (self.__width * self.__height)
        return pmeter