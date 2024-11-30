import unittest
from lab5.task7.src.task7 import *

class TestHeapSort(unittest.TestCase):
    def test_should_make_heapify_max_heap(self):
        # given
        arr = [3, 9, 2, 1, 4]
        n = len(arr)
        i = 0

        # when
        heapify(arr, n, i)

        # then
        self.assertEqual(arr, [9, 4, 2, 1, 3])

    def test_should_make_heapify_partial_heap(self):
        # given
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        i = 1

        # when
        heapify(arr, n, i)

        # then
        self.assertEqual(arr, [1, 5, 3, 4, 2])

    def test_should_make_heapsort_sorted_array(self):
        # given
        arr = [5, 4, 3, 2, 1]

        # when
        heapsort(arr)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_should_make_heapsort_reverse_sorted_array(self):
        # given
        arr = [1, 2, 3, 4, 5]

        # when
        heapsort(arr)

        # then
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_should_make_heapsort_random_array(self):
        # given
        arr = [4, 10, 3, 5, 1]

        # when
        heapsort(arr)

        # then
        self.assertEqual(arr, [1, 3, 4, 5, 10])

if __name__ == "__main__":
    unittest.main()
