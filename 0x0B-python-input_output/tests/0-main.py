#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))


read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
