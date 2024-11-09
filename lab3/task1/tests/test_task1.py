import unittest
import random
from lab3.task1.src.task1 import randomized_partition, randomized_quick_sort_3way



class TestQuickSortEnhancements(unittest.TestCase):

    def test_should_make_randomized_partition(self):
        arr = [3, 5, 2, 1, 4]
        pivot_index = randomized_partition(arr, 0, len(arr) - 1)
        # Проверка: элементы слева от pivot должны быть меньше или равны pivot, справа - больше
        pivot_value = arr[pivot_index]
        for i in range(pivot_index):
            self.assertLessEqual(arr[i], pivot_value)
        for j in range(pivot_index + 1, len(arr)):
            self.assertGreater(arr[j], pivot_value)

    def test_should_make_randomized_quick_sort_3way_sorted(self):
        arr = [3, 5, 2, 2, 4, 1]
        expected = sorted(arr)
        randomized_quick_sort_3way(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_make_randomized_quick_sort_3way_with_duplicates(self):
        arr = [3, 3, 3, 3, 3]
        expected = sorted(arr)
        randomized_quick_sort_3way(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_make_randomized_quick_sort_3way_large_random(self):
        arr = random.sample(range(-10**9, 10**9), 10**4)
        expected = sorted(arr)
        randomized_quick_sort_3way(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_make_randomized_quick_sort_3way_ordered(self):
        arr = list(range(10**3, 0, -1))  # массив от 1000 до 1
        expected = sorted(arr)
        randomized_quick_sort_3way(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

    def test_should_make_randomized_quick_sort_3way_already_sorted(self):
        arr = list(range(1, 1001))  # уже отсортированный массив
        expected = sorted(arr)
        randomized_quick_sort_3way(arr, 0, len(arr) - 1)
        self.assertEqual(arr, expected)

if __name__ == '__main__':
    unittest.main()
