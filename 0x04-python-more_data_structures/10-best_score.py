#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_int = 0
        max = ""
            for key, value in a_dictionary.items():
                if  value > max_int:
                    max_int = value
                max = key
        return max
