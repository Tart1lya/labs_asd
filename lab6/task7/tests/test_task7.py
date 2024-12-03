import unittest
from lab6.task7.src.task7 import *

class TestCountBeautifulPairs(unittest.TestCase):
    def test_should_work_with_single_beautiful_pair(self):
        # given
        n = 7
        k = 1
        S = "abacaba"
        beautiful_pairs = {('a', 'a')}

        # when
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)

        # then
        self.assertEqual(result, 6)

    def test_should_work_when_no_beautiful_pairs(self):
        # given
        n = 5
        k = 1
        S = "abcde"
        beautiful_pairs = {('a', 'b')}

        # when
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)

        # then
        self.assertEqual(result, 1)

    def test_should_work_when_multiple_beautiful_pairs(self):
        # given
        n = 8
        k = 2
        S = "abbaabba"
        beautiful_pairs = {('a', 'b'), ('b', 'a')}

        # when
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)

        # then
        self.assertEqual(result, 16)

    def test_should_work_with_empty_string(self):
        # given
        n = 0
        k = 0
        S = ""
        beautiful_pairs = set()

        # when
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)

        # then
        self.assertEqual(result, 0)

    def test_should_work_when_duplicate_beautiful_pairs(self):
        # given
        n = 6
        k = 2
        S = "abcabc"
        beautiful_pairs = {('a', 'b'), ('a', 'b')}  # Duplicate pairs

        # when
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)

        # then
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
