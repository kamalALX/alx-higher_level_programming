#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elements = 0
    while num_elements < x:
        try:
            print(f"{my_list[num_elements]}", end="")
        except IndexError:
            break
        else:
            num_elements += 1
    print("")
    return num_elements
