#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
