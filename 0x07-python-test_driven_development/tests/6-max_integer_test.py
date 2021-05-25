#!/usr/bin/python3
"""
Unittest for max_integer([..])  
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittest for max_integer function that find and return the max integer in a list of integers.  
    """
    
    def test_ordered_numbers(self):
        list=[2, 3, 10, 50]
        self.assertEqual(max_integer(list), 50)

    def test_unordered_numbers(self):
        list=[2, 100, 10, 50]
        self.assertEqual(max_integer(list), 100)

    def test_empty_list(self):
        list=[]
        self.assertEqual(max_integer(list), None)

    def test_negative_numbers(self):
        list=[-120, -12, -30, -9]
        self.assertEqual(max_integer(list), -9)

    def test_positive_and_negative(self):
        list=[-12, 3, 0, -10, 90]
        self.assertEqual(max_integer(list), 90)

    def test_whit_character(self):
        list=['l', 'z', 'm', 'y']
        self.assertEqual(max_integer(list), 'z')

    def test_whit_string(self):
        list=["Hello", "World", "School"]
        self.assertEqual(max_integer(list), "World")

    def test_unique_value(self):
        list=[9]
        self.assertEqual(max_integer(list), 9)

if __name__ == "__main__":
  unittest.main()