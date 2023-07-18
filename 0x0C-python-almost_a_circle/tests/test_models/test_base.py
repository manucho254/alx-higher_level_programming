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

    def test_save_json_string_to_file_with_objects(self):
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            data = file.read()
            res = [{"x": 1, "y": 8, "id": 1, "height": 7, "width": 10}, {"x": 2, "y": 0, "id": 2, "height": 4, "width": 2}]
            self.assertEqual(json.loads(data), res)
            self.assertIsInstance(json.loads(data), list)

    def test_save_json_string_to_file_without_objects(self):
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            data = file.read()
            res = []
            self.assertEqual(json.loads(data), res)
            self.assertIsInstance(json.loads(data), list)

    def test_json_string_to_list(self):
        
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}
                ]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)

    def test_json_to_list_with_none_value(self):

        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertIsInstance(list_output, list)

if __name__ == "__main__":
    unittest.main()
