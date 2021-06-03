#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath('..'))

BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
