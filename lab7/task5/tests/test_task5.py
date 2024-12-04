import unittest
from lab7.task5.src.task5 import longest_common_subsequence_3


class TestLongestCommonSubsequence3(unittest.TestCase):

    def test_should_work_when_common_subsequence_exists(self):
        # given
        a = [1, 2, 3]
        b = [2, 1, 3]
        c = [1, 3, 5]

        # when
        result = longest_common_subsequence_3(a, b, c)

        # then
        self.assertEqual(result, 2)

    def test_should_work_when_no_common_subsequence(self):
        # given
        a = [1, 2, 3]
        b = [4, 5, 6]
        c = [7, 8, 9]

        # when
        result = longest_common_subsequence_3(a, b, c)

        # then
        self.assertEqual(result, 0)

    def test_should_work_with_identical_sequences(self):
        # given
        a = [1, 2, 3]
        b = [1, 2, 3]
        c = [1, 2, 3]

        # when
        result = longest_common_subsequence_3(a, b, c)

        # then
        self.assertEqual(result, 3)

    def test_should_work_when_partial_overlap(self):
        # given
        a = [1, 2, 3, 4, 5]
        b = [2, 4, 6, 8]
        c = [4, 5, 6]

        # when
        result = longest_common_subsequence_3(a, b, c)

        # then
        self.assertEqual(result, 1)

    def test_should_work_when_empty_sequences(self):
        # given
        a = []
        b = []
        c = []

        # when
        result = longest_common_subsequence_3(a, b, c)

        # then
        self.assertEqual(result, 0)

    def test_should_work_when_single_element_match(self):
        # given
        a = [1]
        b = [1]
        c = [1]

        # when
        result = longest_common_subsequence_3(a, b, c)

        # then
        self.assertEqual(result, 1)

    def test_should_work_with_large_input(self):
        # given
        a = [1] * 100
        b = [1] * 100
        c = [1] * 100

        # when
        result = longest_common_subsequence_3(a, b, c)

        # then
        self.assertEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
