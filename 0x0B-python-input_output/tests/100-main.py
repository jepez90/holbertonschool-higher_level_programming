#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))


append_after = __import__('100-append_after').append_after

append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
