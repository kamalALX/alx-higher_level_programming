#!/usr/bin/python
def multiple_returns(sentence):
    tuple0 = ()
    if len(sentence) == 0:
        tuple0 = 0, "None"
    else:
        tuple0 = len(sentence), sentence[0]
    return tuple0
