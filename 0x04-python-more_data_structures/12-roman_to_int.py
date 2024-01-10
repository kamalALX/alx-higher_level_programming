#!/usr/bin/python3
def check_char(r):
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for key in rom_n:
        if r == key:
            num = (rom_n[key])
            return num
    return None


def roman_to_int(roman_string):
    intiger, i = 0, 0

    if not roman_string:
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
