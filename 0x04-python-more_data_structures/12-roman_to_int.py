#!/usr/bin/python3
def roman_to_int(roman_string):
    integer = 0
    equivalency = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    if roman_string and type(roman_string) == str:

        equ_values = [equivalency[l] for l in roman_string]

        for i, value in enumerate(equ_values):
            if (len(equ_values[i + 1:]) and max(equ_values[i + 1:]) > value):
                integer -= value
            else:
                integer += value

    return integer
