#!/usr/bin/python3
def pow(a, b):
    power = 1
    if b < 0:
        for number in range(b, 0):
            power /= a
    else:
        for number in range(0, b):
            power *= a
    return power
