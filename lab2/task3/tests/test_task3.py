import unittest

from lab2.task3.src.task3 import merge_sort_and_count


class TestInversionCount(unittest.TestCase):

    def test_should_count_inversion_in_empty_array(self):
        # given
        arr = []
        temp_arr = []

        # when
        inv_count = merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

        # then
        self.assertEqual(inv_count, 0)

    def test_should_count_inversion_in_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]
        temp_arr = [0] * len(arr)

        # when
        inv_count = merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

        # then
        self.assertEqual(inv_count, 0)

    def test_should_count_inversion_in_reversed_array(self):
        # given
        arr = [5, 4, 3, 2, 1]
        temp_arr = [0] * len(arr)

        # when
        inv_count = merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

        # then
        self.assertEqual(inv_count, 10)  # n(n-1)/2 для n = 5

    def test_should_count_inversion_in_random_array(self):
        # given
        arr = [1, 3, 5, 2, 4, 6]
        temp_arr = [0] * len(arr)

        # when
        inv_count = merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

        # then
        self.assertEqual(inv_count, 3)  # Инверсии: (3,2), (5,2), (5,4)

    def test_should_count_inversion_in_large_values(self):
        # given
        arr = [10**9, -10**9]
        temp_arr = [0] * len(arr)

        # when
        inv_count = merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

        # then
        self.assertEqual(inv_count, 1)  # Единственная инверсия (10^9, -10^9)

    def test_should_count_inversion_in_single_element(self):
        # given
        arr = [1]
        temp_arr = [0] * len(arr)

        # when
        inv_count = merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)

        # then
        self.assertEqual(inv_count, 0)

if __name__ == '__main__':
    unittest.main()
