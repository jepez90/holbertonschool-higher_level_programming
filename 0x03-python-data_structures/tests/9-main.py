#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

max_integer = __import__('9-max_integer').max_integer

my_list = [-11, -3, 10]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
