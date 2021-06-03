#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
print ("-----")
my_list = []
print_reversed_list_integer(None)
