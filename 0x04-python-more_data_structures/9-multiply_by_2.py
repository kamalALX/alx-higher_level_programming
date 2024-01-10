#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_copy = a_dictionary.copy()
    for key in dic_copy.keys():
        dic_copy[key] *= 2
    return dic_copy
