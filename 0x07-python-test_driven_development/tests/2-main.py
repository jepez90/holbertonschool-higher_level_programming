#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
