#!/usr/bin/python3
"""Module for test the Base class """
import unittest
from unittest.case import skip
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_1id(self):
        """ check if id is set correctly """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


    def test_2dimensions(self):
        r4 = Rectangle(10, 2)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)

        r4.width = 13
        r4.height = 8
        self.assertEqual(r4.width, 13)
        self.assertEqual(r4.height, 8)

        self.assertRaises(TypeError, Rectangle, "e", 10)
        self.assertRaises(TypeError, Rectangle, 10, "10")

        self.assertRaises(ValueError, Rectangle, -8, 10)
        self.assertRaises(ValueError, Rectangle, 10, 0)

    def test_position(self):
        r4 = Rectangle(10, 2)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

        r4 = Rectangle(10, 2, 10, 2)
        self.assertEqual(r4.x, 10)
        self.assertEqual(r4.y, 2)

        r4.x = 13
        r4.y = 8
        self.assertEqual(r4.x, 13)
        self.assertEqual(r4.y, 8)

        self.assertRaises(TypeError, Rectangle, 10, 10, "e", 10)
        self.assertRaises(TypeError, Rectangle, 10, 10, 0, "10")

        self.assertRaises(ValueError, Rectangle, 10, 10, -8, 10)
        self.assertRaises(ValueError, Rectangle, 10, 10, 10, -1)

