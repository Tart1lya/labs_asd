import unittest

from lab7.task6.src.task6 import find_lis  # Замените на актуальный путь к вашей функции


class TestFindLIS(unittest.TestCase):

    def test_should_work_when_simple_case(self):
        # given
        n = 5
        sequence = [10, 20, 10, 30, 20]

        # when
        lis_length, lis_sequence = find_lis(n, sequence)

        # then
        self.assertEqual(lis_length, 3)
        self.assertEqual(lis_sequence, [10, 20, 30])

    def test_should_work_when_sorted_sequence(self):
        # given
        n = 4
        sequence = [1, 2, 3, 4]

        # when
        lis_length, lis_sequence = find_lis(n, sequence)

        # then
        self.assertEqual(lis_length, 4)
        self.assertEqual(lis_sequence, [1, 2, 3, 4])

    def test_should_work_when_reversed_sequence(self):
        # given
        n = 4
        sequence = [4, 3, 2, 1]

        # when
        lis_length, lis_sequence = find_lis(n, sequence)

        # then
        self.assertEqual(lis_length, 1)
        self.assertEqual(lis_sequence, [1])

    def test_should_work_with_single_element(self):
        # given
        n = 1
        sequence = [42]

        # when
        lis_length, lis_sequence = find_lis(n, sequence)

        # then
        self.assertEqual(lis_length, 1)
        self.assertEqual(lis_sequence, [42])

    def test_should_work_when_all_equal_elements(self):
        # given
        n = 5
        sequence = [7, 7, 7, 7, 7]

        # when
        lis_length, lis_sequence = find_lis(n, sequence)

        # then
        self.assertEqual(lis_length, 1)
        self.assertEqual(lis_sequence, [7])

    def test_should_work_with_alternating_sequence(self):
        # given
        n = 6
        sequence = [1, 3, 2, 4, 3, 5]

        # when
        lis_length, lis_sequence = find_lis(n, sequence)

        # then
        self.assertEqual(lis_length, 4)
        self.assertEqual(lis_sequence, [1, 2, 3, 5])

    def test_should_work_with_large_values(self):
        # given
        n = 4
        sequence = [1000000000, 999999999, 1000000000, 1000000001]

        # when
        lis_length, lis_sequence = find_lis(n, sequence)

        # then
        self.assertEqual(lis_length, 3)
        self.assertEqual(lis_sequence, [999999999, 1000000000, 1000000001])

if __name__ == "__main__":
    unittest.main()
