import unittest
from lab1.task5.src.task5 import selection_sort


class TestSelectionSort(unittest.TestCase):

    def test_should_sort_sorted_list(self):
        # given
        n = 5
        m = [1, 2, 3, 4, 5]

        # when
        selection_sort(n, m)

        # then
        self.assertEqual(m, [1, 2, 3, 4, 5])

    def test_should_sort_reverse_sorted_list(self):
        # given
        n = 5
        m = [5, 4, 3, 2, 1]

        # when
        selection_sort(n, m)

        # then
        self.assertEqual(m, [1, 2, 3, 4, 5])

    def test_should_sort_unsorted_list(self):
        # given
        n = 6
        m = [31, 41, 59, 26, 41, 58]

        # when
        selection_sort(n, m)

        # then
        self.assertEqual(m, [26, 31, 41, 41, 58, 59])

    def test_should_sort_single_element_list(self):
        # given
        n = 1
        m = [42]

        # when
        selection_sort(n, m)

        # then
        self.assertEqual(m, [42])

    def test_should_sort_empty_list(self):
        # given
        n = 0
        m = []

        # when
        selection_sort(n, m)

        # then
        self.assertEqual(m, [])

    def test_should_sort_large_numbers(self):
        # given
        n = 3
        m = [10**9, -10**9, 0]

        # when
        selection_sort(n, m)

        # then
        self.assertEqual(m, [-10**9, 0, 10**9])


if __name__ == '__main__':
    unittest.main()
