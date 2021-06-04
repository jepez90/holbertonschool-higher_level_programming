#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
