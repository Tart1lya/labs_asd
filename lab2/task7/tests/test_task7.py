import unittest

from lab2.task7.src.task7 import max_subarray



class TestMaxSubarray(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_subarray([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(max_subarray([1, -1, 2, 3]), [1, -1, 2, 3])

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), [4, -1, 2, 1])
        self.assertEqual(max_subarray([-1, -2, -3, -4]), [-1])

    def test_zeroes(self):
        self.assertEqual(max_subarray([0, 0, 0]), [0])
        self.assertEqual(max_subarray([-1, 0, 1]), [0, 1])

    def test_single_element(self):
        self.assertEqual(max_subarray([5]), [5])
        self.assertEqual(max_subarray([-1]), [-1])

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            max_subarray([])