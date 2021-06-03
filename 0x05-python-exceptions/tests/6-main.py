#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
