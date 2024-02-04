#!/usr/bin/python3
""" a module that contain a class called BaseGeometry . """


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
