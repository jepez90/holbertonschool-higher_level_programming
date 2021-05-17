#!/usr/bin/python3
def safe_print_division(a, b):
    division = 0
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    finally:
        try:
            print("Inside result: {:.1f}".format(division))
        except TypeError:
            print("Inside result: None")
    return division
