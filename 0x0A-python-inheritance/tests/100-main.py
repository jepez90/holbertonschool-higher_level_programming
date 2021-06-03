#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath('..'))

MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
