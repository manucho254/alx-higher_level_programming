#!/usr/bin/python3
""" tests for Base Model
"""
import unittest
import json

from models.base import Base
from models.rectangle import Rectangle

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)

class TestBase(unittest.TestCase):

    def setUp(self):
        self.base = Base(12)

    def test_base_initialization_with_value(self):
        self.assertEqual(self.base.id, 12)

    def test_convert_to_json_string(self):
        new_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([new_dict])
        self.assertIsInstance(new_dict, dict)
        res = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(json_dictionary, res)

    def test_convert_to_json_string(self):
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            data = file.read()
            res = [{"x": 1, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 2, "y": 0, "id": 2, "height": 4, "width": 2}]
            self.assertEqual(json.loads(data), res)
            self.assertIsInstance(json.loads(data), list)


if __name__ == "__main__":
    unittest.main()
