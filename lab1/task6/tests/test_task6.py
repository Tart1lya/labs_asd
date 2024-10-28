import unittest
from lab1.task6.src.task6 import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_sorted_list(self):
        n = 5
        m = [1, 2, 3, 4, 5]
        bubble_sort(n, m)
        self.assertEqual(m, [1, 2, 3, 4, 5])  # Список уже отсортирован

    def test_reverse_sorted_list(self):
        n = 5
        m = [5, 4, 3, 2, 1]
        bubble_sort(n, m)
        self.assertEqual(m, [1, 2, 3, 4, 5])  # Проверка сортировки

    def test_unsorted_list(self):
        n = 6
        m = [31, 41, 59, 26, 41, 58]
        bubble_sort(n, m)
        self.assertEqual(m, [26, 31, 41, 41, 58, 59])  # Проверка на произвольном списке

    def test_single_element_list(self):
        n = 1
        m = [42]
        bubble_sort(n, m)
        self.assertEqual(m, [42])  # Список с одним элементом

    def test_empty_list(self):
        n = 0
        m = []
        bubble_sort(n, m)
        self.assertEqual(m, [])  # Пустой список

    def test_large_numbers(self):
        n = 3
        m = [10**9, -10**9, 0]
        bubble_sort(n, m)
        self.assertEqual(m, [-10**9, 0, 10**9])  # Сортировка с большими числами

if __name__ == '__main__':
    unittest.main()
