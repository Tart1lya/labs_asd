import unittest
from lab3.task3.src.task3 import can_sort


class TestCanSort(unittest.TestCase):

    def test_should_print_can_sort_possible(self):
        # given
        n = 6
        m = 2
        arr = [3, 1, 2, 4, 6, 5]

        # when
        result = can_sort(n, m, arr)

        # then
        self.assertEqual(result, "НЕТ")

    def test_should_print_can_sort_impossible(self):
        # given
        n = 6
        m = 3
        arr = [3, 1, 2, 4, 6, 5]

        # when
        result = can_sort(n, m, arr)

        # then
        self.assertEqual(result, "НЕТ")

    def test_should_print_with_single_element(self):
        # given
        n = 1
        m = 1
        arr = [10]

        # when
        result = can_sort(n, m, arr)

        # then
        self.assertEqual(result, "ДА")

    def test_should_print_with_identical_elements(self):
        # given
        n = 5
        m = 2
        arr = [7, 7, 7, 7, 7]

        # when
        result = can_sort(n, m, arr)

        # then
        self.assertEqual(result, "ДА")

    def test_should_print_with_large_input(self):
        # given
        n = 10 ** 5
        m = 2
        arr = list(range(10 ** 5, 0, -1))

        # when
        result = can_sort(n, m, arr)

        # then
        self.assertEqual(result, "НЕТ")


if __name__ == '__main__':
    unittest.main()
