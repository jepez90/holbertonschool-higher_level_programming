#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

my_rectangle.width = 0
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))
print(my_rectangle)
print(repr(my_rectangle))
