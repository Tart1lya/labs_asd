import unittest

from lab2.task5.src.task5 import majority_element_rec, count_occurrences


class TestMajorityElement(unittest.TestCase):

    def test_should_majority_element_present(self):
        # given
        arr = [2, 3, 9, 2, 2]
        n = len(arr)

        # when
        result = majority_element_rec(arr, 0, n)

        # then
        self.assertEqual(result, 2)

    def test_should_no_majority_element(self):
        # given
        arr = [1, 2, 3, 4]
        n = len(arr)

        # when
        result = majority_element_rec(arr, 0, n)

        # then
        self.assertIsNone(result)

    def test_should_single_element(self):
        # given
        arr = [5]
        n = len(arr)

        # when
        result = majority_element_rec(arr, 0, n)

        # then
        self.assertEqual(result, 5)

    def test_should_two_elements_majority(self):
        # given
        arr = [4, 4, 4, 4, 2, 2, 4, 4]
        n = len(arr)

        # when
        result = majority_element_rec(arr, 0, n)

        # then
        self.assertEqual(result, 4)

    def test_should_count_occurrences(self):
        # given
        arr = [2, 3, 9, 2, 2]
        num = 2

        # when
        count = count_occurrences(arr, num, 0, len(arr))

        # then
        self.assertEqual(count, 3)

    def test_should_large_array(self):
        # given
        arr = [1] * 50000 + [2] * 50000
        n = len(arr)

        # when
        result = majority_element_rec(arr, 0, n)

        # then
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()