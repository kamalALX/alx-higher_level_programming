#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_new = list(a_dictionary.keys())
    for val_dic in list_new:
        if value == a_dictionary.get(val_dic):
                del a_dictionary[val_dic]
    return (a_dictionary)
