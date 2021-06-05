#!/usr/bin/python3
"""Module for test the Base class """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ This calass test the base class """

    def test_id(self):
        """ check if id is set correctly """

        base = Base()
        self.assertEqual(base.id, 1)
        base2 = Base()
        base4 = Base(12)
        base3 = Base()
        self.assertEqual(base2.id, 2)
        self.assertEqual(base4.id, 12)
        self.assertEqual(base3.id, 3)
        self.assertRaises(TypeError, Base().__init__, "12")
