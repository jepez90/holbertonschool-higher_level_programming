#!/usr/bin/python3
import os
import sys
sys.path.append(os.path.abspath('..'))

is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class


class MyClass1():
    pass


class MyClass2(MyClass1):

    my_attr1 = 3

    def my_meth(self):
        pass


a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))


a = MyClass1()
if is_kind_of_class(a, MyClass1):
    print("{} comes from {}".format(str(a), MyClass1.__name__))
if is_kind_of_class(a, MyClass2):
    print("{} comes from {}".format(str(a), MyClass2.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(str(a), object.__name__))

a = MyClass2()
if is_kind_of_class(a, MyClass1):
    print("{} comes from {}".format(a, MyClass1.__name__))
if is_kind_of_class(a, MyClass2):
    print("{} comes from {}".format(a, MyClass2.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
