#!/usr/bin/python3

""" This module defines a class called "Rectangle" """
from models.base import Base


class Rectangle(Base):
    """ this class represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ inisialization method
            Args:
                width (int):
                height (int):
                x (int):
                y (int):
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ returns the area value of the Rectangle instance. """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle instance with
            the character # plus handling the
            position of the rectangle when printing it using
            x and y.
        """
        print('\n' * self.__y, end='')
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """ String representation of the class rectangle """
        return "[Rectangle] (" + str(self.id) + ')' + ' ' +\
            str(self.__x) + '/' + str(self.__y) + ' ' + '-' + ' ' +\
            str(self.__width) + '/' + str(self.__height)

    def update(self, *args, **kwargs):
        """ this method assigns an argument to each attribute """
        if args is not None and len(args) != 0:
            list0 = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, list0[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
