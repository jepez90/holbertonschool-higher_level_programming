#!/usr/bin/python3
import os, sys
sys.path.append(os.path.abspath('..'))

matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6], [5, 6]]))
