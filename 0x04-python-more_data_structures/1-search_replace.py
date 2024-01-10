#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replace_element = lambda element: replace if element == search else element
    new_list = list(map(replace_element, my_list))
    return new_list
