#!/usr/bin/python3
""" Test Square Class
"""
import unittest

from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(4, 5, 6, 12)

    def test_initialize_square_no_arguments(self):
        with self.assertRaises(TypeError):
            self.square = Square()

    def test_initialize_rectangle_1_argument(self):
        self.square = Square(4)
        self.square.id = 1

        self.assertEqual(self.square.width, 4)
        self.assertEqual(self.square.height, 4)
        self.assertEqual(self.square.x, 0)
        self.assertEqual(self.square.y, 0)
        self.assertEqual(self.square.id, 1)

    def test_initialize_rectangle_all_arguments(self):

        self.assertEqual(self.square.width, 4)
        self.assertEqual(self.square.height, 4)
        self.assertEqual(self.square.x, 5)
        self.assertEqual(self.square.y, 6)
        self.assertEqual(self.square.id, 12)


if __name__ == "__main__":
    unittest.main()
