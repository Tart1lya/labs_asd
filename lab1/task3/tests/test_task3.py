import unittest
from lab1.task3.src.task3 import descending_sort


class TestDescendingSort(unittest.TestCase):

    def test_should_sort_sorted_list(self):
        # given
        n = 5
        m = [5, 4, 3, 2, 1]

        # when
        descending_sort(n, m)

        # then
        self.assertEqual(m, [5, 4, 3, 2, 1])  # Список уже отсортирован по убыванию

    def test_should_sort_reverse_sorted_list(self):
        # given
        n = 5
        m = [1, 2, 3, 4, 5]

        # when
        descending_sort(n, m)

        # then
        self.assertEqual(m, [5, 4, 3, 2, 1])  # Проверяем сортировку

    def test_should_sort_unsorted_list(self):
        # given
        n = 6
        m = [31, 41, 59, 26, 41, 58]

        # when
        descending_sort(n, m)

        # then
        self.assertEqual(m, [59, 58, 41, 41, 31, 26])  # Проверяем на произвольном списке

    def test_should_sort_single_element_list(self):
        # given
        n = 1
        m = [42]

        # when
        descending_sort(n, m)

        # then
        self.assertEqual(m, [42])  # Список с одним элементом

    def test_should_sort_empty_list(self):
        # given
        n = 0
        m = []

        # when
        descending_sort(n, m)

        # then
        self.assertEqual(m, [])  # Пустой список

    def test_should_sort_large_numbers(self):
        # given
        n = 3
        m = [10**9, -10**9, 0]

        # when
        descending_sort(n, m)

        # then
        self.assertEqual(m, [10**9, 0, -10**9])  # Сортировка с большими числами


if __name__ == '__main__':
    unittest.main()
