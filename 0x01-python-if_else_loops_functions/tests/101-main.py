#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))


remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Holberton School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
