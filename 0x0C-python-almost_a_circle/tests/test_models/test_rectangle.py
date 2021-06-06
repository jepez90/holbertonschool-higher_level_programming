#!/usr/bin/python3
"""Module for test the Base class """
import unittest
from unittest.case import skip
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_1id(self):
        """ check if id is set correctly, the name of function is _1id so that
        it is the first test to be executed and the number of closed instances
        starts at 0.
        """

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1, 'error at set first id')

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2, 'error at set second id')

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12, 'error at give id in the constructor')

    def test_dimensions(self):
        """ check if the dimensions width y height are validates and sets
        correctly
        """

        r4 = Rectangle(10, 2)
        self.assertEqual(r4.width, 10, 'error at set width in constructor')
        self.assertEqual(r4.height, 2, 'error at set height in constructor')

        r4.width = 13
        r4.height = 8
        self.assertEqual(r4.width, 13, 'error at set width in setter')
        self.assertEqual(r4.height, 8, 'error at set height in setter')

        self.assertRaises(TypeError, Rectangle, "e", 10)
        self.assertRaises(TypeError, Rectangle, 10, "10")

        self.assertRaises(ValueError, Rectangle, -8, 10)
        self.assertRaises(ValueError, Rectangle, 10, 0)

    def test_position(self):
        """ check if the position x y y are validates and sets correctly """

        r4 = Rectangle(10, 2)
        self.assertEqual(r4.x, 0, 'don´t set 0 as default x')
        self.assertEqual(r4.y, 0, 'don´t set 0 as default y')

        r4 = Rectangle(10, 2, 10, 2)
        self.assertEqual(r4.x, 10,
                         'don´t set the given value of x in the constructor')
        self.assertEqual(r4.y, 2,
                         'don´t set the given value of y in the constructor')

        r4.x = 13
        r4.y = 8
        self.assertEqual(r4.x, 13,
                         'don´t set the given value of x in the setter')
        self.assertEqual(r4.y, 8,
                         'don´t set the given value of y in the setter')

        self.assertRaises(TypeError, Rectangle, 10, 10, "e", 10)
        self.assertRaises(TypeError, Rectangle, 10, 10, 0, "10")

        self.assertRaises(ValueError, Rectangle, 10, 10, -8, 10)
        self.assertRaises(ValueError, Rectangle, 10, 10, 10, -1)

    def test_area(self):
        """ check if the area is calculate correctly """

        r5 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r5.area(), 6, 'don´t calc the area correctly')
        r5.width = 1
        self.assertEqual(r5.area(), 3, 'don´t calc the area correctly')
        r5.height = 1
        self.assertEqual(r5.area(), 1, 'don´t calc the area correctly')

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
            self.assertEqual(fake_out.getvalue(), expected_out,
                             'error at display a rectangle of 1 x 1')

        r6.width = 2
        r6.height = 3
        expected_out = '##\n##\n##\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), expected_out,
                             'error at display a rectangle of 3 x 2')
        r6.x = 1
        r6.y = 3
        expected_out = '\n\n\n ##\n ##\n ##\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), expected_out,
                             'error at display a rect 3 x 2 in position 1 x 3')

        r6.x = 4
        r6.y = 1
        r6.width = 1
        r6.height = 1
        expected_out = '\n    #\n'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            r6.display()
            self.assertEqual(fake_out.getvalue(), expected_out,
                             'error at display a rect 3 x 2 in position 1 x 3')

    def test_update_args(self):
        """ test the update function with arguments by 'no-keyword argument'
        way """

        r7 = Rectangle(1, 2)
        r7.update()

        r7.update(6)
        self.assertEqual(r7.id, 6,
                         'don´t uptdate only one argument (id) correctly.')

        r7.update(10, 7)
        self.assertEqual(r7.id, 10,
                         'don´t uptdate the first argument (id) correctly.')
        self.assertEqual(r7.area(), 14,
                         'don´t uptdate the second argument (id) correctly.')

        r7.update(10, 8, 8)
        self.assertEqual(r7.area(), 64,
                         'don´t uptdate any argument (id) correctly.')

        r7.update(6, 3, 10, 19, 14)
        self.assertEqual(r7.id, 6,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(r7.area(), 30,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(r7.x, 19,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(r7.y, 14,
                         'don´t uptdate any argument (id) correctly.')

    def test_update_kwargs(self):
        """ test the update function with arguments by 'key-worded argument'
        way """

        r8 = Rectangle(1, 2)
        # void dict ??????????????????????????????
        # r8.update({})

        r8.update(id=6)
        self.assertEqual(r8.id, 6,
                         'don´t uptdate only one argument (id) correctly.')

        r8.update(id=10, width=7)
        self.assertEqual(r8.id, 10,
                         'don´t uptdate the first argument (id) correctly.')
        self.assertEqual(r8.area(), 14,
                         'don´t uptdate the second argument (id) correctly.')

        r8.update(y=14, height=10, id=6, x=19, width=3)
        self.assertEqual(r8.id, 6,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(r8.area(), 30,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(r8.x, 19,
                         'don´t uptdate any argument (id) correctly.')
        self.assertEqual(r8.y, 14,
                         'don´t uptdate any argument (id) correctly.')
