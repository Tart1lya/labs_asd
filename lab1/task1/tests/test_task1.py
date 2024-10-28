import unittest

from lab1.task1.src.task1 import insertion_sort



class TestInsertionSort(unittest.TestCase):

    def test_sorted_list(self):
        m = [1, 2, 3, 4, 5]
        insertion_sort(len(m), m)
        self.assertEqual(m, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        m = [5, 4, 3, 2, 1]
        insertion_sort(len(m), m)
        self.assertEqual(m, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        m = [31, 41, 59, 26, 41, 58]
        insertion_sort(len(m), m)
        self.assertEqual(m, [26, 31, 41, 41, 58, 59])

    def test_single_element_list(self):
        m = [42]
        insertion_sort(len(m), m)
        self.assertEqual(m, [42])

    def test_empty_list(self):
        m = []
        insertion_sort(len(m), m)
        self.assertEqual(m, [])

    def test_negative_numbers(self):
        m = [-3, -1, -7, -4, -5]
        insertion_sort(len(m), m)
        self.assertEqual(m, [-7, -5, -4, -3, -1])

    def test_large_numbers(self):
        m = [10 ** 9, -10 ** 9, 0, 10 ** 8, -10 ** 8]
        insertion_sort(len(m), m)
        self.assertEqual(m, [-10 ** 9, -10 ** 8, 0, 10 ** 8, 10 ** 9])


if __name__ == '__main__':
    unittest.main()
