#!/usr/bin/python3
"""Module to find the point product of two matrix
"""


def matrix_mul(m_a, m_b):
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
    # check for the type of the both argument
    type_list_error = '{} must be a list'
    if type(m_a) != list:
        raise TypeError(type_list_error.format('m_a'))
    if type(m_b) != list:
        raise TypeError(type_list_error.format('m_b'))

    # check for the type of each elemets of the list
    type_each_list_error = '{} must be a list of lists'
    for element in m_a:
        if type(element) != list:
            raise TypeError(type_each_list_error.format('m_a'))
    for element in m_b:
        if type(element) != list:
            raise TypeError(type_each_list_error.format('m_b'))

    # check of the type elemets of the each list
    empty_list_error = '{} can\'t be empty'
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError(empty_list_error.format('m_a'))
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError(empty_list_error.format('m_b'))

    # check if any list is empty
    type_each_element_error = '{} should contain only integers or floats'
    for row in m_a:
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError(type_each_element_error.format('m_a'))
    for row in m_b:
        for element in row:
            if type(element) != int and type(element) != float:
                raise TypeError(type_each_element_error.format('m_b'))

    # check if any list in the list have diferent length
    diferent_length_error = "each row of {} must be of the same size"
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError(diferent_length_error.format('m_a'))
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError(diferent_length_error.format('m_b'))

    # check if list can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []

    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            number = 0
            for k in range(len(m_b)):
                number += (m_a[i][k] * m_b[k][j])
            new_row.append(number)
        new_matrix.append(new_row)

    return new_matrix
