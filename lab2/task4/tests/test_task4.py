import unittest

from lab2.task4.src.task4 import binary_search



class TestBinarySearch(unittest.TestCase):

    def test_should_binary_search_found(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 7), 3)

    def test_should_binary_search_not_found(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 6), -1)

    def test_should_binary_search_first_element(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 1), 0)

    def test_should_binary_search_last_element(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search(arr, 9), 4)

    def test_should_binary_search_empty_array(self):
        arr = []
        self.assertEqual(binary_search(arr, 1), -1)
