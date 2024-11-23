import unittest

from lab2.task7.src.task7 import max_subarray


class TestMaxSubarray(unittest.TestCase):

    def test_positive_numbers(self):
        # given
        arr = [1, 2, 3, 4, 5]

        # when
        result = max_subarray(arr)

        # then
        self.assertEqual(result, [1, 2, 3, 4, 5])

        # given
        arr = [1, -1, 2, 3]

        # when
        result = max_subarray(arr)

        # then
        self.assertEqual(result, [1, -1, 2, 3])

    def test_mixed_numbers(self):
        # given
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

        # when
        result = max_subarray(arr)

        # then
        self.assertEqual(result, [4, -1, 2, 1])

        # given
        arr = [-1, -2, -3, -4]

        # when
        result = max_subarray(arr)

        # then
        self.assertEqual(result, [-1])

    def test_zeroes(self):
        # given
        arr = [0, 0, 0]

        # when
        result = max_subarray(arr)

        # then
        self.assertEqual(result, [0])

        # given
        arr = [-1, 0, 1]

        # when
        result = max_subarray(arr)

        # then
        self.assertEqual(result, [0, 1])

    def test_single_element(self):
        # given
        arr = [5]

        # when
        result = max_subarray(arr)

        # then
        self.assertEqual(result, [5])

        # given
        arr = [-1]

        # when
        result = max_subarray(arr)

        # then
        self.assertEqual(result, [-1])

    def test_empty_array(self):
        # given
        arr = []

        # when & then
        with self.assertRaises(IndexError):
            max_subarray(arr)
