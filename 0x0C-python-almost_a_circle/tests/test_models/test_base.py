""" tests for Base Model
"""
import unittest

from models.base import Base

class TestBaseClass(unittest.TestCase):

    def setUp(self):
        self.base = Base()

    def test_base_initialization_no_value_1(self):
        self.assertEqual(self.base.id, 1)

    def test_base_initialization_with_value(self):
        self.base = Base(12)

        self.assertEqual(self.base.id, 12)

    def test_base_initialization_no_value_2(self):
        self.assertEqual(self.base.id, 2)

    def test_base_initialization_no_value_3(self):
        self.assertEqual(self.base.id, 3)
