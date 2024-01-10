#!/usr/bin/python3
def best_score(a_dictionary):
    max_int = 0
    max = ""
    if a_dictionary == None:
        return None
    else:
        for key, value in a_dictionary.items():
            if  value > max_int:
                max_int = value
            max = key
    return max
