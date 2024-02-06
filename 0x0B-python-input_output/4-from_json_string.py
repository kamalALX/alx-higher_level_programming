#!/usr/bin/python3
""" Defines a function that Convert from JSON to Python object"""
import json


def to_json_string(my_obj):
    """ Return: object (Python data structure) represented by a JSON string"""
    return json.loads(my_obj)
