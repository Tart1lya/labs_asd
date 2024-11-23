import unittest

from lab1.task1.src.task1 import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_should_sort_sorted_list(self):
        # given
        m = [1, 2, 3, 4, 5]

        # when
        insertion_sort(len(m), m)

        # then
        self.assertEqual(m, [1, 2, 3, 4, 5])

    def test_should_sort_reverse_sorted_list(self):
        # given
        m = [5, 4, 3, 2, 1]

        # when
        insertion_sort(len(m), m)

        # then
        self.assertEqual(m, [1, 2, 3, 4, 5])

    def test_should_sort_unsorted_list(self):
        # given
        m = [31, 41, 59, 26, 41, 58]

        # when
        insertion_sort(len(m), m)

        # then
        self.assertEqual(m, [26, 31, 41, 41, 58, 59])

    def test_should_sort_single_element_list(self):
        # given
        m = [42]

        # when
        insertion_sort(len(m), m)

        # then
        self.assertEqual(m, [42])

    def test_should_sort_empty_list(self):
        # given
        m = []

        # when
        insertion_sort(len(m), m)

        # then
        self.assertEqual(m, [])

    def test_should_sort_negative_numbers(self):
        # given
        m = [-3, -1, -7, -4, -5]

        # when
        insertion_sort(len(m), m)

        # then
        self.assertEqual(m, [-7, -5, -4, -3, -1])

    def test_should_sort_large_numbers(self):
        # given
        m = [10 ** 9, -10 ** 9, 0, 10 ** 8, -10 ** 8]

        # when
        insertion_sort(len(m), m)

        # then
        self.assertEqual(m, [-10 ** 9, -10 ** 8, 0, 10 ** 8, 10 ** 9])


if __name__ == '__main__':
    unittest.main()
