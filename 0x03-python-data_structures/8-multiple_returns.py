#!/usr/bin/python
def multiple_returns(sentence):
    tuple0 = ()
    if len(sentence) == 0:
        return 0, "None"
    else:
        return len(sentence), sentence[0]
