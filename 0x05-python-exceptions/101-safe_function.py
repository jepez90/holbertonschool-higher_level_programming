#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a, b = args
        return fct(a, b)
    except:
        print("Exception:", sys.exc_info()[1], file=sys.stderr)
        return None
