#!/usr/bin/python3
""" module for pascal_triangle function

inputs:
- an integer n
output:
- a list of lists of integers
  when the first number is  and each number of the list is the result
  of the sum of two previos numbers in the triangle
edge cases:
- n < 0: return an empty list.
- n is not an integer.

step by step:
- create a list of lists
- crate the first list with the number 1 and
    add this list to the triangle only if n > 0
- define an iteration from 1 to n (i)
    - add the first element from the first element of the previous list
    - create the new row
    - define a nested loop to first iterator less 1 (j)
         - add to row the add of the two numbers of the previous row
    - add the last number of the previous list
    - add the list to the matrix
return the matrix
"""


def pascal_triangle(n):
    """ calculate the pascal's triangle with n rows and returns it
    """
    # create the list of lists
    triangle = []
    if n > 0:
        # first add the list with number 1
        triangle.append([1])
        for i in range(1, n):
            # for to add rows to the triangle
            previous_row = triangle[i - 1]
            row = [1]

            for j in range(i - 1):
                # add the sum of the numbers in the previous row
                number = previous_row[j] + previous_row[j + 1]
                row.append(number)
            row.append(1)
            triangle.append(row)

    return triangle
