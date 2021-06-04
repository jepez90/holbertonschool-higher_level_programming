#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))


print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
