#!/usr/bin/python3
""" a module that contain a class called BaseGeometry. """


class BaseGeometry:
    """ a class BaseGeometry """
    def area(self):
        """ raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ a method that validates value """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """ a class BaseGeometry """
    def __init__(self, width, height):
        """ Initiator method.
            Args:
            width (int): width of the Rectangle.
            height (int): height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def are(self):
        """ this method returns the area of a rectangle """
        return self.__width * self.__height

    def __print__(self):
        """ String representation of the class """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))


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
