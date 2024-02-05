#!/usr/bin/python3
""" a module that contain a class called BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def __str__(self):
        """ String representation of the class """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
