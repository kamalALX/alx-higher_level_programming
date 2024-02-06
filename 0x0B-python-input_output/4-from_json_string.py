#!/usr/bin/python3
""" Defines a function that Convert from JSON to Python object"""
import json


def from_json_string(my_str):
    """ Return: object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
