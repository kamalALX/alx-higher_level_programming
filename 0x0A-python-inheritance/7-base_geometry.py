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
            raise TypeError("{} must be an integer".formay(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
