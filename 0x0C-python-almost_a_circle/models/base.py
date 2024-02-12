#!/usr/bin/python3

""" class Base"""
import json


class Base:
    """ class Base"""
    __nb__objects = 0

    def __init__(self, id=None):
        """ initializaion method """
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converts a python object into a json """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """

        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ convert from json string to python """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

        @classmethod
        def create(cls, **dictionary):
            """ returns an instance with all attributes already set """
            if dictionary and dictionary != {}:
                if cls.__name__ == "Rectangle":
                    dummy = cls(1, 1)
                else:
                    dummy = cls(1)
                dummy.update(**dictionary)
                return dummy
