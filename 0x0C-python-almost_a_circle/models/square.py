#!/usr/bin/python3

""" this module contains the definition of class  "Square" """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization method """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ String representation of the class rectangle """
        return "[Square] (" + str(self.id) + ')' + ' ' +\
            str(self.x) + '/' + str(self.y) + ' ' + '-' + ' ' +\
            str(self.size)

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ this method assigns attributes """
        if args is not None and len(args) != 0:
            list1 = ['id', 'size', 'x', 'y']
            i = 0
            for arg in args:
                if list1[i] == 'size':
                    setattr(self, 'width', arg)
                    setattr(self, 'height', arg)
                else:
                    setattr(self, list1[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        list3 = ['id', 'size', 'x', 'y']
        diction = {}
        for i in range(4):
            diction[list3[i]] = getattr(self, list3[i])
        return diction
