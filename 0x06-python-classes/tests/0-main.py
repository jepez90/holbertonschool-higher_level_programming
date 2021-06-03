#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
