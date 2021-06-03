#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'Track': {"a":"Low level", "c": "vbdfgbfg", "b": "fbv"}, 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
