#!/usr/bin/python3
""" an empty class Rectangle that defines a rectangle """


class Rectangle:

    """ a class that defines a rectangle
        Attributes:
            number_of_instances(int): The number of Rectangle instances.
            print_symbol (any): used for string representation.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initializes a new Rectangle.
        Args:
            width(int): represents the width of the new rectangle
            height(int): represents the height of the new rectangle
        """
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        return slef.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ returns the rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the rectangle perimeter """
        pmeter = 2 * (self.__width * self.__height)
        return pmeter

    def __str__(self):
        """returns the representation of the rectangle with the character # """
        if not self.__width or not self.__height:
            return ""
        listt = []
        for i in range(self.__height):
            for j in range(self.__width):
                listt.append('#')
            listt.append('\n')
        return ("".join(listt))

    def __repr__(self):
        """ returns a string representation of the rectangle """
        st = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return st

    def __del__(self):
        """ prints a string when a rectangle object is
            deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
