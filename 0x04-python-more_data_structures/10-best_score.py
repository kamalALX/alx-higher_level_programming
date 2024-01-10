#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        list0 = list(a_dictionary.keys())
        max_int = 0
        max = ""
        for key in list0:
            if a_dictionary[key] > max_int:
                max_int = a_dictionary[key]
                max = key
        return max
