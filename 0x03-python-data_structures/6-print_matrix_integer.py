#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, number in enumerate(row):
            if (i != 0):
                # prints an space before the number if it doesn't the firt
                print(" ", end="")
            # print the number
            print("{:d}".format(number), end="")
        print()
