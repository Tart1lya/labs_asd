import unittest
from lab1.task6.src.task6 import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_should_sort_sorted_list(self):
        # given
        n = 5
        m = [1, 2, 3, 4, 5]

        # when
        bubble_sort(n, m)

        # then
        self.assertEqual(m, [1, 2, 3, 4, 5])  # Список уже отсортирован

    def test_should_sort_reverse_sorted_list(self):
        # given
        n = 5
        m = [5, 4, 3, 2, 1]

        # when
        bubble_sort(n, m)

        # then
        self.assertEqual(m, [1, 2, 3, 4, 5])  # Проверка сортировки

    def test_should_sort_unsorted_list(self):
        # given
        n = 6
        m = [31, 41, 59, 26, 41, 58]

        # when
        bubble_sort(n, m)

        # then
        self.assertEqual(m, [26, 31, 41, 41, 58, 59])  # Проверка на произвольном списке

    def test_should_sort_single_element_list(self):
        # given
        n = 1
        m = [42]

        # when
        bubble_sort(n, m)

        # then
        self.assertEqual(m, [42])  # Список с одним элементом

    def test_should_sort_empty_list(self):
        # given
        n = 0
        m = []

        # when
        bubble_sort(n, m)

        # then
        self.assertEqual(m, [])  # Пустой список

    def test_should_sort_large_numbers(self):
        # given
        n = 3
        m = [10**9, -10**9, 0]

        # when
        bubble_sort(n, m)

        # then
        self.assertEqual(m, [-10**9, 0, 10**9])  # Сортировка с большими числами


if __name__ == '__main__':
    unittest.main()
