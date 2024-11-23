import unittest

from lab2.task4.src.task4 import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_should_binary_search_found(self):
        # given
        arr = [1, 3, 5, 7, 9]
        target = 7

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, 3)

    def test_should_binary_search_not_found(self):
        # given
        arr = [1, 3, 5, 7, 9]
        target = 6

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, -1)

    def test_should_binary_search_first_element(self):
        # given
        arr = [1, 3, 5, 7, 9]
        target = 1

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, 0)

    def test_should_binary_search_last_element(self):
        # given
        arr = [1, 3, 5, 7, 9]
        target = 9

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, 4)

    def test_should_binary_search_empty_array(self):
        # given
        arr = []
        target = 1

        # when
        result = binary_search(arr, target)

        # then
        self.assertEqual(result, -1)
