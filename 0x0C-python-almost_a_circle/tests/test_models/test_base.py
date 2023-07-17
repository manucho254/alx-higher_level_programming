#!/usr/bin/python3
""" tests for Base Model
"""
import unittest

from models.base import Base


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


if __name__ == "__main__":
    unittest.main()
