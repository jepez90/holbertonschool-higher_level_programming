#!/usr/bin/python3
"""Module to test the function max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """this class test the function max_integer
    """
    def test_max_integer(self):
        # test max integer when exist many types in the list
        self.assertAlmostEqual(max_integer([1, 2, 5, 4]), 5)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([-3, -4]), -3)

        #test for rise correct errors
        self.assertRaises(TypeError, max_integer, [10, 10.1])
        self.assertRaises(TypeError, max_integer, [10, '10'])
        self.assertRaises(TypeError, max_integer, [10, 's'])
        self.assertRaises(TypeError, max_integer, {'a': 10, 'b': 12})
        self.assertRaises(TypeError, max_integer, 'hola')
        self.assertRaises(TypeError, max_integer, None)
