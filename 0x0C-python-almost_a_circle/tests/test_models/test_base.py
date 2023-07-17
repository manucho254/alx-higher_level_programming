#!/usr/bin/python3
""" tests for Base Model
"""
import unittest

from models.base import Base


class TestBase(unittest.TestCase):

    """ def test_base_initialization_no_value(self):
        self.base = Base()
        self.assertEqual(self.base.id, 1)
        del self.base """

    def test_base_initialization_with_value(self):
        self.base = Base(12)
        self.assertEqual(self.base.id, 12)
        del self.base


if __name__ == "__main__":
    unittest.main()
