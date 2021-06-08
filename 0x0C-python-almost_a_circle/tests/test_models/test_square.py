#!/usr/bin/python3
"""Module for test the Square class """
import unittest
from unittest.case import skip
# to check std output
from io import StringIO
from unittest.mock import patch

from models.square import Square


class TestSquare(unittest.TestCase):
    """ Class with the tests for the square class """

    def test_1id(self):
        """ check if id is set correctly, the name of function is _1id so that
        it is the first test to be executed and the number of closed instances
        starts at 0.
        """

        s1 = Square(10)
        self.assertEqual(s1.id, 1, 'error at set first id')

        s2 = Square(4, 10, 3)
        self.assertEqual(s2.id, 2, 'error at set second id')

        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s3.id, 12, 'error at give id in the constructor')

    def test_dimensions(self):
        """ check if the dimension size is validates and sets correctly """

        s4 = Square(10)
        self.assertEqual(s4.size, 10, 'error at set size in constructor')
        self.assertEqual(s4.width, 10, 'error at set width in size settes')
        self.assertEqual(s4.height, 10, 'error at set height in size settes')

        s4.size = 13
        self.assertEqual(s4.size, 13, 'error at set size in setter')
        self.assertEqual(s4.width, 13, 'error at set size in setter')
        self.assertEqual(s4.height, 13, 'error at set size in setter')

        self.assertRaises(ValueError, Square, 0)

    def test_str(self):
        """ check if the printable representation is correct """

        s9 = Square(4, 2, 1, 12)
        self.assertEqual(str(s9), '[Square] (12) 2/1 - 4')
        s10 = Square(5)
        s10.id = 16
        self.assertEqual(str(s10), '[Square] (16) 0/0 - 5')

    def test_update_args(self):
        """ test the update function with arguments by 'no-keyword argument'
        way """

        s7 = Square(1)
        s7.update()

        s7.update(6)
        self.assertEqual(s7.id, 6,
                         'don´t uptdate only one argument (id) correctly.')

        s7.update(10, 7)
        self.assertEqual(s7.id, 10,
                         'don´t uptdate the first argument (id) correctly.')

        self.assertEqual(s7.area(), 7 * 7,
                         'don´t uptdate the second argument (size) correctly.')

        s7.update(6, 3, 19, 14)
        self.assertEqual(s7.id, 6,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(s7.area(), 3 * 3,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(s7.x, 19,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(s7.y, 14,
                         'don´t uptdate any argument (id) correctly.')

    def test_update_kwargs(self):
        """ test the update function with arguments by 'key-worded argument'
        way """

        s8 = Square(1)
        # void dict ??????????????????????????????
        # r8.update({})

        s8.update(id=6)
        self.assertEqual(s8.id, 6,
                         'don´t uptdate only one argument (id) correctly.')

        s8.update(id=10, size=7)
        self.assertEqual(s8.id, 10,
                         'don´t uptdate the first argument (id) correctly.')
        self.assertEqual(s8.area(), 7 * 7,
                         'don´t uptdate the second argument (id) correctly.')

        s8.update(y=14, size=10, id=6, x=19)
        self.assertEqual(s8.id, 6,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(s8.area(), 10**2,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(s8.x, 19,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(s8.y, 14,
                         'don´t uptdate any argument (id) correctly.')
