#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (5, 5))
my_square_3.my_print()

print("--")
