#!/usr/bin/python3
"""Module for test the Base class """
import unittest
from unittest.case import skip
# to check std output
from io import StringIO
from unittest.mock import patch

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_1id(self):
        """ check if id is set correctly, the name of function is _1id so that
        it is the first test to be executed and the number of closed instances
        starts at 0.
        """

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12,)

    def test_dimensions(self):
        """ check if the dimensions width y height are validates and sets
        correctly
        """

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
        self.assertRaises(ValueError, Rectangle, 8, -10)

        self.assertRaises(ValueError, Rectangle, 10, 0)
        self.assertRaises(ValueError, Rectangle, 0, 10)

    def test_position(self):
        """ check if the position x y y are validates and sets correctly """

        r4 = Rectangle(10, 2)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

        r4 = Rectangle(10, 2, 10)
        self.assertEqual(r4.x, 10)
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

    def test_area(self):
        """ check if the area is calculate correctly """

        r5 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r5.area(), 6)
        r5.width = 1
        self.assertEqual(r5.area(), 3)
        r5.height = 1
        self.assertEqual(r5.area(), 1)

    def test_str(self):
        """ check if the printable representation is correct """

        r9 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r9), '[Rectangle] (12) 2/1 - 4/6')
        r10 = Rectangle(5, 5)
        r10.id = 16
        self.assertEqual(str(r10), '[Rectangle] (16) 0/0 - 5/5')

    def test_display(self):
        """ check if the display function show the rectangle correctly """
        r6 = Rectangle(1, 1)
        expected_out = '#\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), expected_out)

        r6.width = 2
        r6.height = 3
        expected_out = '##\n##\n##\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), expected_out)
        r6.x = 1
        r6.y = 3
        expected_out = '\n\n\n ##\n ##\n ##\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), expected_out)

        r6.x = 1
        r6.y = 0
        expected_out = ' ##\n ##\n ##\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), expected_out)

        r6.x = 4
        r6.y = 1
        r6.width = 1
        r6.height = 1
        expected_out = '\n    #\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), expected_out)

    def test_update_args(self):
        """ test the update function with arguments by 'no-keyword argument'
        way """

        r7 = Rectangle(1, 2)
        r7.update()

        r7.update(6)
        self.assertEqual(r7.id, 6)

        r7.update(10, 7)
        self.assertEqual(r7.id, 10)
        self.assertEqual(r7.area(), 7 * 2)

        r7.update(10, 8, 8)
        self.assertEqual(r7.area(), 8 * 8)

        r7.update(10, 8, 9, 10)
        self.assertEqual(r7.area(), 8 * 9)
        self.assertEqual(r7.x, 10)

        r7.update(6, 3, 10, 19, 14)
        self.assertEqual(r7.id, 6)
        self.assertEqual(r7.area(), 3 * 10)
        self.assertEqual(r7.x, 19)
        self.assertEqual(r7.y, 14)

        self.assertRaises(TypeError, r7.update(), 6, "3", 10, 19, 14)

    def test_update_kwargs(self):
        """ test the update function with arguments by 'key-worded argument'
        way """

        r8 = Rectangle(1, 2)
        # void dict ??????????????????????????????
        # r8.update({})

        r8.update(id=6)
        self.assertEqual(r8.id, 6)

        r8.update(id=10, width=7)
        self.assertEqual(r8.id, 10)
        self.assertEqual(r8.area(), 14)

        r8.update(id=10, width=7, height=8)
        self.assertEqual(r8.id, 10)
        self.assertEqual(r8.area(), 7 * 8)

        r8.update(id=10, width=7, height=8, x=9)
        self.assertEqual(r8.id, 10)
        self.assertEqual(r8.area(), 7 * 8)
        self.assertEqual(r8.x, 9)

        r8.update(y=14, height=10, id=6, x=19, width=3)
        self.assertEqual(r8.id, 6)
        self.assertEqual(r8.area(), 30)
        self.assertEqual(r8.x, 19)
        self.assertEqual(r8.y, 14)

    def test_to_dicttionary(self):
        """ check if to_dictionary returns the dict correctly """
        r9 = Rectangle(4, 6, 8, 3, 12)
        expect_out = {'id': 12, 'width': 4, 'height': 6, 'x': 8, 'y': 3}
        self.assertEqual(r9.to_dictionary(), expect_out)

    def test_to_json_string(self):
        """ check if return the correct json string from a list of dicts """
        r10 = Rectangle(3, 4)
        r10.id = 18
        expect_out = '[{"height": 4, "id": 18, "width": 3, "x": 0, "y": 0}, '\
            '{"a": 1}]'
        self.assertEqual(Rectangle.to_json_string([r10.to_dictionary(),
                                                   {"a": 1}]), expect_out)
