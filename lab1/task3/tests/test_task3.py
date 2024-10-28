import unittest
from lab1.task3.src.task3 import descending_sort

class TestDescendingSort(unittest.TestCase):

    def test_sorted_list(self):
        n = 5
        m = [5, 4, 3, 2, 1]
        descending_sort(n, m)
        self.assertEqual(m, [5, 4, 3, 2, 1])  # Список уже отсортирован по убыванию

    def test_reverse_sorted_list(self):
        n = 5
        m = [1, 2, 3, 4, 5]
        descending_sort(n, m)
        self.assertEqual(m, [5, 4, 3, 2, 1])  # Проверяем сортировку

    def test_unsorted_list(self):
        n = 6
        m = [31, 41, 59, 26, 41, 58]
        descending_sort(n, m)
        self.assertEqual(m, [59, 58, 41, 41, 31, 26])  # Проверяем на произвольном списке

    def test_single_element_list(self):
        n = 1
        m = [42]
        descending_sort(n, m)
        self.assertEqual(m, [42])  # Список с одним элементом

    def test_empty_list(self):
        n = 0
        m = []
        descending_sort(n, m)
        self.assertEqual(m, [])  # Пустой список

    def test_large_numbers(self):
        n = 3
        m = [10**9, -10**9, 0]
        descending_sort(n, m)
        self.assertEqual(m, [10**9, 0, -10**9])  # Сортировка с большими числами

if __name__ == '__main__':
    unittest.main()
