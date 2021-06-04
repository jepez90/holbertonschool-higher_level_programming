#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))


uppercase = __import__('8-uppercase').uppercase

uppercase("holberton")
uppercase("Holberton School 98 Battery street")
