#!/usr/bin/python3
def no_c(my_string):
    string = list(my_string)
    for idx in range(len(string)):
        if string[idx] == 'c' or string[idx] == 'C':
            string[idx] = ''
    return "".join(string)
