import unittest
from lab1.task2.src.task2 import insertion_sort_plus


class TestInsertionSortPlus(unittest.TestCase):

    def test_should_sort_sorted_list(self):
        # given
        n = 5
        m = [1, 2, 3, 4, 5]
        indices = [1]

        # when
        insertion_sort_plus(n, m, indices)

        # then
        self.assertEqual(m, [1, 2, 3, 4, 5])
        self.assertEqual(indices, [1, 2, 3, 4, 5])

    def test_should_sort_reverse_sorted_list(self):
        # given
        n = 5
        m = [5, 4, 3, 2, 1]
        indices = [1]

        # when
        insertion_sort_plus(n, m, indices)

        # then
        self.assertEqual(m, [1, 2, 3, 4, 5])
        self.assertEqual(indices, [1, 1, 1, 1, 1])

    def test_should_sort_unsorted_list(self):
        # given
        n = 6
        m = [31, 41, 59, 26, 41, 58]
        indices = [1]

        # when
        insertion_sort_plus(n, m, indices)

        # then
        self.assertEqual(m, [26, 31, 41, 41, 58, 59])
        self.assertEqual(indices, [1, 2, 3, 1, 4, 5])

    def test_should_sort_single_element_list(self):
        # given
        n = 1
        m = [42]
        indices = [1]

        # when
        insertion_sort_plus(n, m, indices)

        # then
        self.assertEqual(m, [42])
        self.assertEqual(indices, [1])

    def test_should_sort_empty_list(self):
        # given
        n = 0
        m = []
        indices = []

        # when
        insertion_sort_plus(n, m, indices)

        # then
        self.assertEqual(m, [])
        self.assertEqual(indices, [])

    def test_should_sort_large_numbers(self):
        # given
        n = 3
        m = [10**9, -10**9, 0]
        indices = [1]

        # when
        insertion_sort_plus(n, m, indices)

        # then
        self.assertEqual(m, [-10**9, 0, 10**9])
        self.assertEqual(indices, [1, 1, 2])


if __name__ == '__main__':
    unittest.main()
