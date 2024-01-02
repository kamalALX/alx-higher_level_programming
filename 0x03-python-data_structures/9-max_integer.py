#!/usr/bin/python3

def max_integer(my_list=[]):
    max = 0
    if len(my_list) == 0:
        return None

    for i in range (len(my_list)):
        number = my_list[i]
        if (number > max):
            max = number
    return max
