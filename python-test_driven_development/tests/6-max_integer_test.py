#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_positive_integers(self):
        """Test with a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        """Test with a list of mixed positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([-10, -20, 0, 20]), 20)

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_list_with_same_elements(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3, -4.4]), -1.1)

    def test_mixed_floats_and_integers(self):
        """Test with a list of mixed floats and integers."""
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)
        self.assertEqual(max_integer([-1.1, -2, -3.3, -4]), -1.1)

    def test_string_input(self):
        """Test with a string input."""
        self.assertEqual(max_integer("abcdef"), 'f')
        self.assertEqual(max_integer("zyx"), 'z')

    def test_empty_string(self):
        """Test with an empty string."""
        self.assertIsNone(max_integer(""))

    def test_list_of_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none_input(self):
        """Test with None as input."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
