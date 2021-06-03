#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath('..'))
lookup = __import__('0-lookup').lookup


class MyClass1():
    pass


class MyClass2():

    my_attr1 = 3

    def my_meth(self):
        pass

print(lookup(MyClass1))
print()
print(MyClass1.__dict__)
print()
print(lookup(MyClass2))
print()
print()
print(lookup(int))
print()
print(int.__dict__)
