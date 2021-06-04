#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))


fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")
