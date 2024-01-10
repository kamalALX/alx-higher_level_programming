#!/usr/bin/python3
def check_char(r):
    if r == 'I':
        return 1
    elif r == 'V':
        return 5
    elif r == 'X':
        return 10
    elif r == 'L':
        return 50
    elif r == 'C':
        return 100
    elif r == 'D':
        return 500
    elif r == 'M':
        return 1000

    return 0


def roman_to_int(roman_string):
    intiger, i = 0, 0

    if not roman_string or not isinstance(roman_string, str):
        return 0

    while i < len(roman_string):
        if i + 1 < len(roman_string):
            if roman_string[i] == 'I' and roman_string[i + 1] == 'V':
                intiger += 4
                i += 2
            elif roman_string[i] + roman_string[i + 1] == 'IX':
                intiger += 9
                i += 2
            elif roman_string[i] + roman_string[i + 1] == 'XL':
                intiger += 40
                i += 2
            elif roman_string[i] + roman_string[i] == 'CD':
                intiger += 400
                i += 2
        if i < len(roman_string):
            intiger += check_char(roman_string[i])
            i += 1

    return intiger
