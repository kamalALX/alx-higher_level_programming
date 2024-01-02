#!/usr/bin/python

def multiple_returns(sentence):
    cr_tuple = (sentence)
    if (len(sentence) == 0):
        return 0, None
    return len(cr_tuple), cr_tuple[0]
