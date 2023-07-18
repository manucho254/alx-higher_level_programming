#!/usr/bin/python3
""" tests for rectangle class
"""
import unittest
from unittest.mock import patch
import io
import sys

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

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
        # self.assertEqual(self.rectangle.id, 1)

    def test_initialize_rectangle_3_arguments(self):
        self.rectangle = Rectangle(5, 4, 2)

        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 0)
        # self.assertEqual(self.rectangle.id, 2)

    def test_initialize_rectangle_4_arguments(self):
        self.rectangle = Rectangle(5, 4, 2, 6)

        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 4)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 6)
        # self.assertEqual(self.rectangle.id, 3)


class TestRectangleValidation(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(5, 4, 2, 6, 12)

    def test_validate_width_value_type(self):
        with self.assertRaises(TypeError):
            self.rectangle.width = "2"

    def test_validate_width_less_than_1(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = -1

    def test_validate_height_value_type(self):

        with self.assertRaises(TypeError):
            self.rectangle.height = "2"

    def test_validate_height_less_than_1(self):
        with self.assertRaises(ValueError):
            self.rectangle.height = -1

    def test_validate_x_value_type(self):
        with self.assertRaises(TypeError):
            self.rectangle.y = {8, 9}

    def test_validate_x_value_type(self):
        with self.assertRaises(ValueError):
            self.rectangle.x = -4

    def test_validate_y_value_type(self):
        with self.assertRaises(TypeError):
            self.rectangle.y = [1, 2]

    def test_validate_y_value_type(self):
        with self.assertRaises(ValueError):
            self.rectangle.y = -2


class TestRectangleMethods(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(5, 4, 2, 6, 12)
        self.area = self.rectangle.area()
        self._old_stdout = sys.stdout
        sys.stdout = io.TextIOWrapper(io.BytesIO(), sys.stdout.encoding)

    def test_get_area(self):
        self.assertEqual(self.area, 20)

    def test_get_area_type(self):
        self.assertIsInstance(self.area, int)

    def test_display_rectangle(self):
        self.rectangle.display()
        sys.stdout.seek(0)
        msg = "\n\n\n\n\n\n  #####\n  #####\n  #####\n  #####\n"
        self.assertEqual(sys.stdout.read(), msg)

    def test_rectangle_string_representation(self):
        r1 = Rectangle(5, 5, 1)
        r2 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), f"[Rectangle] ({r1.id}) 1/0 - 5/5")
        self.assertEqual(str(r2), f"[Rectangle] (12) 2/1 - 4/6")

    def test_update_method_with_args(self):
        self.rectangle = Rectangle(10, 10, 10, 10)

        message = f"[Rectangle] ({self.rectangle.id}) 10/10 - 10/10"
        self.assertEqual(str(self.rectangle), message)
        self.rectangle.update(89)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 10/10 - 10/10")
        self.rectangle.update(89, 2)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 10/10 - 2/10")
        self.rectangle.update(89, 2, 3)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 10/10 - 2/3")
        self.rectangle.update(89, 2, 3, 4)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 4/10 - 2/3")
        self.rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_method_with_kwargs(self):
        self.rectangle = Rectangle(10, 10, 10, 10)

        message = f"[Rectangle] ({self.rectangle.id}) 10/10 - 10/10"
        self.assertEqual(str(self.rectangle), message)
        self.rectangle.update(height=1)
        message = f"[Rectangle] ({self.rectangle.id}) 10/10 - 10/1"
        self.assertEqual(str(self.rectangle), message)
        self.rectangle.update(width=1, x=2)
        message = f"[Rectangle] ({self.rectangle.id}) 2/10 - 1/1"
        self.assertEqual(str(self.rectangle), message)
        self.rectangle.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.rectangle), f"[Rectangle] (89) 3/1 - 2/1")
        self.rectangle.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(self.rectangle), f"[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary_method(self):
        self.rectangle = Rectangle(10, 2, 1, 9, 1)

        message = f"[Rectangle] (1) 1/9 - 10/2"
        self.assertEqual(str(self.rectangle), message)
        message = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        to_dict = self.rectangle.to_dictionary()
        self.assertEqual(to_dict, message)
        self.assertIsInstance(to_dict, dict)

    def tearDown(self):
        sys.stdout.close()
        sys.stdout = self._old_stdout


if __name__ == "__main__":
    unittest.main()
