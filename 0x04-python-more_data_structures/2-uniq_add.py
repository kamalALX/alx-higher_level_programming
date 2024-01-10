#!/usr/bin/python3
def uniq_add(my_list=[]):
    rm_duplicates = list(set(my_list))
    sum = 0
    for i in range(len(rm_duplicates)):
        sum += rm_duplicates[i]
    return sum
