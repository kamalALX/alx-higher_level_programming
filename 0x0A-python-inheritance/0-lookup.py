#!/usr/bin/python3
""" A module that contain the lookup method"""


def lookup(obj):
    """A function that returns a list of all
        avaliables attributes and methods of an object.
    Args:
        obj (object): the object to list.
    Return: A list object.
    """
    return dir(obj)
