#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))


add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
