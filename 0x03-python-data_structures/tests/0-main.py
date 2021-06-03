#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))


print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
