import unittest

from lab5.task4.src.task4 import *

class TestBuildMinHeap(unittest.TestCase):
    def test_should_make_min_heap_example_1(self):
        # given
        data = [5, 4, 3, 2, 1]

        # when
        swaps = build_min_heap(data)

        # then
        self.assertEqual(data, [1, 2, 3, 5, 4])
        self.assertEqual(swaps, [(1, 4), (0, 1), (1, 3)])

    def test_should_make_min_heap_example_2(self):
        # given
        data = [7, 6, 5, 4, 3, 2, 1]

        # when
        swaps = build_min_heap(data)

        # then
        self.assertEqual(data, [1, 3, 2, 4, 6, 7, 5])
        self.assertEqual(swaps, [(2, 6), (1, 4), (0, 2), (2, 5)])

    def test_should_make_min_heap_when_already_heap(self):
        # given
        data = [1, 2, 3, 4, 5]

        # when
        swaps = build_min_heap(data)

        # then
        self.assertEqual(data, [1, 2, 3, 4, 5])
        self.assertEqual(swaps, [])

    def test_should_make_min_heap_with_single_element(self):
        # given
        data = [42]

        # when
        swaps = build_min_heap(data)

        # then
        self.assertEqual(data, [42])
        self.assertEqual(swaps, [])

    def test_should_make_min_heap_with_two_elements(self):
        # given
        data = [2, 1]

        # when
        swaps = build_min_heap(data)

        # then
        self.assertEqual(data, [1, 2])
        self.assertEqual(swaps, [(0, 1)])


if __name__ == "__main__":
    unittest.main()
