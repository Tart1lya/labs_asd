import unittest

from lab2.task1.src.task1 import merge_sort



class TestMergeSort(unittest.TestCase):

    def test_should_sort_random(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected = sorted(arr)
        merge_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_sort_empty(self):
        arr = []
        expected = []
        merge_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_sort_single_element(self):
        arr = [42]
        expected = [42]
        merge_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = arr[:]
        merge_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_sort_reverse_order(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = sorted(arr)
        merge_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_sort_large_array(self):
        # Тест с большим массивом (максимально допустимый размер)
        arr = list(range(2 * 10 ** 4, 0, -1))
        expected = sorted(arr)
        merge_sort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

if __name__ == '__main__':
    unittest.main()
