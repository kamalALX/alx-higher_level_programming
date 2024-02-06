#!/usr/bin/python3
""" defiens a function that write a text into a file """


def write_file(filename="", text=""):
    """ write 'text' into 'filename'
        Return: the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
