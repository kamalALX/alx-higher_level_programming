#!/usr/bin/python3
def islower(c):
    c = ord(c)
    for lowercase in range(97, 123):
        if c is lowercase:
            return True
    return False
