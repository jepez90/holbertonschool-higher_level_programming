#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath('..'))

Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(str(r))
print(r.area())
