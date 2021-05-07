#!/usr/bin/python3
def val_of_symbol(symbol):
    equivalency = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    return equivalency[symbol]


def roman_to_int(roman_string):
    integer = 0

    if roman_string is None and type(roman_string) == str:

        equ_values = [val_of_symbol(l) for l in roman_string]

        for i, value in enumerate(equ_values):
            if (i + 1 != len(equ_values) and max(equ_values[i + 1:]) > value):
                integer -= value
            else:
                integer += value

    return integer
