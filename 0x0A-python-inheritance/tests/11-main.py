#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath('..'))

Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
