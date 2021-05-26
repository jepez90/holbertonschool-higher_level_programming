#!/usr/bin/python3
"""multiply two matrix and return the matrix result"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiply two matrix and return the matrix result

    Args:
        m_a ([[int]]): first matrix to be multiplied
        m_b ([[int]]): second matrix to be multiplied

    Returns:
        [[int]]: new matrix with the result

    Raises:
        TypeError: when any argument is not an list of lists of integers
        ValueError: when any list is empty or the matrix can't be multiplied
    """


    # check for the type of each elemets of the list
    type_each_list_error = '{} must be a list of lists'
    for element in m_a:
        if type(element) != list:
            raise TypeError(type_each_list_error.format('m_a'))
    for element in m_b:
        if type(element) != list:
            raise TypeError(type_each_list_error.format('m_b'))

    a = np.array(m_a)
    b = np.array(m_b)

    return((a.dot(b)).tolist())
