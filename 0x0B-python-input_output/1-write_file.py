#!/usr/bin/python3
""" defiens a function that write a text into a file """


def write_file(filename="", text=""):
    """ write 'text' into 'filename' """
    with open(filename, "w", wencoding="utf-8") as f:
        return f.write(text)
