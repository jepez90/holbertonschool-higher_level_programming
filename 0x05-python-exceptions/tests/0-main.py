#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [True, 2, 3, "4", 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, 8)
print("nb_print: {:d}".format(nb_print))
