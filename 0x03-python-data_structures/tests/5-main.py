#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

no_c = __import__('5-no_c').no_c

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
print(no_c("Cccc"))
