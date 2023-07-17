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


class TestSquareValidation(unittest.TestCase):

    def test_square_size_type(self):
        with self.assertRaises(TypeError):
            square = Square("4")

    def test_square_size_less_than_1(self):
        with self.assertRaises(ValueError):
            square = Square(-2)


class TestSquareMethods(unittest.TestCase):
    
    def setUp(self):
        self.square = Square(5)

    def test_get_size(self):
        self.assertEqual(self.square.size, 5)

    def test_update_size(self):
        self.square.size =  8

        self.assertEqual(self.square.size, 8)

    def test_update_method_with_args(self):

        message = f"[Square] ({self.square.id}) 0/0 - 5"
        self.assertEqual(str(self.square), message)
        self.square.update(10)
        message = f"[Square] ({self.square.id}) 0/0 - 5"
        self.assertEqual(str(self.square), message)
        self.square.update(1, 2)
        message = f"[Square] ({self.square.id}) 0/0 - 2"
        self.assertEqual(str(self.square), message)
        self.square.update(1, 2, 3)
        message = f"[Square] ({self.square.id}) 3/0 - 2"
        self.assertEqual(str(self.square), message)
        self.square.update(1, 2, 3, 4)
        message = f"[Square] ({self.square.id}) 3/4 - 2"
        self.assertEqual(str(self.square), message)

    def test_update_method_with_kwargs(self):
        self.square = Square(5) 

        self.square.update(x=12)
        message = f"[Square] ({self.square.id}) 12/0 - 5"
        self.assertEqual(str(self.square), message)
        self.square.update(size=7, y=1)
        message = f"[Square] ({self.square.id}) 12/1 - 7"
        self.assertEqual(str(self.square), message)
        self.square.update(size=7, id=89, y=1)
        message = f"[Square] (89) 12/1 - 7"
        self.assertEqual(str(self.square), message)

    def test_to_dictionary_method(self):
        self.square = Square(10, 2, 1)

        message = f"[Square] ({self.square.id}) 2/1 - 10"
        self.assertEqual(str(self.square), message)
        message = {'id': self.square.id, 'x': 2, 'size': 10, 'y': 1}
        to_dict = self.square.to_dictionary()
        self.assertEqual(to_dict, message)
        self.assertIsInstance(to_dict, dict)


if __name__ == "__main__":
    unittest.main()
