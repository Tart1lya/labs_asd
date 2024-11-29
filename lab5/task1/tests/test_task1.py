import unittest
from lab5.task1.src.task1 import *

class TestIsHeap(unittest.TestCase):
    def test_should_work_with_valid_heap(self):
        # given
        array = [1, 2, 3, 4, 5, 6]
        n = len(array)

        # when
        result = is_heap(array, n)

        # then
        self.assertTrue(result)

    def test_should_work_with_invalid_heap(self):
        # given
        array = [1, 0, 1, 2, 0]
        n = len(array)

        # when
        result = is_heap(array, n)

        # then
        self.assertFalse(result)

    def test_should_work_with_single_element(self):
        # given
        array = [10]
        n = len(array)

        # when
        result = is_heap(array, n)

        # then
        self.assertTrue(result)

    def test_should_work_with_two_elements_which_are_valid(self):
        # given
        array = [1, 2]
        n = len(array)

        # when
        result = is_heap(array, n)

        # then
        self.assertTrue(result)

    def test_should_work_with_two_elements_which_are_invalid(self):
        # given
        array = [2, 1]
        n = len(array)

        # when
        result = is_heap(array, n)

        # then
        self.assertFalse(result)

    def test_should_work_with_large_valid_heap(self):
        # given
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = len(array)

        # when
        result = is_heap(array, n)

        # then
        self.assertTrue(result)

    def test_should_work_with_large_invalid_heap(self):
        # given
        array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        n = len(array)

        # when
        result = is_heap(array, n)

        # then
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
