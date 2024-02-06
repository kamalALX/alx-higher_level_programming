#!/usr/bin/python3
""" defiens a function that appends a text to a text file """


def append_write(filename="", text=""):
    """ append 'text' to the end of 'filename'
        Return: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
