import unittest
from lab7.task4.src.task4 import longest_common_subsequence


class TestLongestCommonSubsequence(unittest.TestCase):

    def test_should_work_with_common_elements(self):
        # given
        n = 3
        A = [2, 7, 5]
        m = 2
        B = [2, 5]

        # when
        result = longest_common_subsequence(n, A, m, B)

        # then
        self.assertEqual(result, 2)

    def test_should_work_when_no_common_elements(self):
        # given
        n = 3
        A = [1, 2, 3]
        m = 3
        B = [4, 5, 6]

        # when
        result = longest_common_subsequence(n, A, m, B)

        # then
        self.assertEqual(result, 0)

    def test_should_work_with_identical_sequences(self):
        # given
        n = 4
        A = [1, 2, 3, 4]
        m = 4
        B = [1, 2, 3, 4]

        # when
        result = longest_common_subsequence(n, A, m, B)

        # then
        self.assertEqual(result, 4)

    def test_should_work_when_one_empty_sequence(self):
        # given
        n = 0
        A = []
        m = 5
        B = [1, 2, 3, 4, 5]

        # when
        result = longest_common_subsequence(n, A, m, B)

        # then
        self.assertEqual(result, 0)

    def test_should_work_with_different_lengths(self):
        # given
        n = 6
        A = [1, 3, 5, 7, 9, 11]
        m = 3
        B = [3, 7, 10]

        # when
        result = longest_common_subsequence(n, A, m, B)

        # then
        self.assertEqual(result, 2)

    def test_should_work_when_repeated_elements(self):
        # given
        n = 5
        A = [1, 2, 2, 3, 4]
        m = 4
        B = [2, 2, 4, 5]

        # when
        result = longest_common_subsequence(n, A, m, B)

        # then
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
