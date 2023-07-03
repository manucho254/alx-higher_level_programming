#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ class to test max_integer function
    """
    def setUp(self):
        """ function to declare defaults for class
        """
        self.arr = []

    def test_invalid_list(self):
        """ checks for datatypes that are not lists
        """
        with self.assertRaises(TypeError):
            max_integer(max_integer(30))

    def test_empty_list(self):
        """ checks for empty lists
        """
        self.assertEqual(max_integer(self.arr), None)
        self.assertEqual(max_integer(), None)

    def test_valid_list(self):
        """ checks for a valid list
        """
        self.arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(self.arr), 5)

    def test_duplicate_max_value(self):
        """ checks for lists with duplicate max values
        """
        self.arr = [1, 2, 3, 4, 5, 5]
        self.assertEqual(max_integer(self.arr), 5)

    def test_negative_values(self):
        """ checks for lists with negative values
        """
        self.arr = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(self.arr), -1)

    def test_invalid_data_type_in_list(self):
        """ checks for list with invlid datatypes """
        self.arr = [1, "test", [1, 2]]
        with self.assertRaises(TypeError): 
            max_integer(self.arr)

    def test_for_strings(self):
        self.assertEqual(max_integer("testing"), "t")

    def test_for_list_with_strings(self):
        self.arr = ["testing", "cool"]
        self.assertEqual(max_integer(self.arr), "testing")

if __name__ == "__main__":
    unittest.main()
