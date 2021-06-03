#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath('..'))

BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
