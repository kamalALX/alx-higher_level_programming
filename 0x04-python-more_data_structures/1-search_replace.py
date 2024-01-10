#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_1 = (lambda element: replace if element == search else element)
    new_list = list(map(replace_1, my_list))
    return new_list
