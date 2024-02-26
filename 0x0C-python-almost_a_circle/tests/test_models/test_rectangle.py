#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.

Unittest classes

"""
from io import StringIO
from unittest.mock import patch
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_width_type(self):
        self.assertRaises(TypeError, Rectangle, "1", 2)

    def test_height_type(self):
        self.assertRaises(TypeError, Rectangle, 1, "2")

    def test_x_type(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, "3", 4, 7)

    def test_y_type(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, "4", 7)

    def test_width_value(self):
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, -1, 2)

    def test_height_value(self):
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertRaises(ValueError, Rectangle, 1, -1)

    def test_x_value(self):
        self.assertRaises(ValueError, Rectangle, 1, 2, -1, 4, 7)

    def test_y_value(self):
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4, 7)

    def test_rectangle_area(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_str_(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).__str__(),
                         "[Rectangle] (5) 3/4 - 1/2")

    def test_rectangle_display(self):
        s = Rectangle(1, 2)
        with patch('sys.stdout', new=StringIO()) as output:
            exp = "#\n#\n"
            s.display()
            got = output.getvalue()
            self.assertEqual(got, exp)

        s = Rectangle(1, 2, 1, 1)
        with patch('sys.stdout', new=StringIO()) as output:
            exp = "\n #\n #\n"
            s.display()
            got = output.getvalue()
            self.assertEqual(got, exp)
