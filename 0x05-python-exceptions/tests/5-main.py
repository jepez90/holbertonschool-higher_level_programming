#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
