#!/usr/bin/python3

""" tests for rectangle class
"""
import unittest

from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(5, 4, 2, 6, 12)

    def test_initialize_rectangle_no_arguments(self):
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle()

    def test_initialize_rectangle_1_argument(self):
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(4)

    def test_initialize_rectangle_2_arguments(self):
        self.rectangle = Rectangle(5, 4)

        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 0)
        self.assertEqual(self.rectangle.y, 0)
        self.assertEqual(self.rectangle.id, 1)

    def test_initialize_rectangle_3_arguments(self):
        self.rectangle = Rectangle(5, 4, 2)

        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 0)
        self.assertEqual(self.rectangle.id, 2)

    def test_initialize_rectangle_4_arguments(self):
        self.rectangle = Rectangle(5, 4, 2, 6)

        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 6)
        self.assertEqual(self.rectangle.id, 3)

    def test_initialize_rectangle_all_arguments(self):

        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 6)
        self.assertEqual(self.rectangle.id, 12)


if __name__ == "__main__":
    unittest.main()
