#!/usr/bin/python3
""" defines a function that read a text file """


def read_file(filename=""):
    """ print the text in the file """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
