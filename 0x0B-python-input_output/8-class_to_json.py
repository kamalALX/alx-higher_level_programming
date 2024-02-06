#!/usr/bin/python3
""" defines a function that returns """


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
