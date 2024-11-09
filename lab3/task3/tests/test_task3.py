import unittest
from lab3.task3.src.task3 import can_sort



class TestCanSort(unittest.TestCase):

    def test_should_print_can_sort_possible(self):
        # Проверяем случай, когда сортировка возможна
        result = can_sort(6, 2, [3, 1, 2, 4, 6, 5])
        self.assertEqual(result, "НЕТ")

    def test_should_print_can_sort_impossible(self):
        # Проверяем случай, когда сортировка невозможна
        result = can_sort(6, 3, [3, 1, 2, 4, 6, 5])
        self.assertEqual(result, "НЕТ")

    def test_should_print_with_single_element(self):
        # Проверяем случай с одним элементом
        result = can_sort(1, 1, [10])
        self.assertEqual(result, "ДА")

    def test_should_print_with_identical_elements(self):
        # Проверяем случай, когда все элементы одинаковы
        result = can_sort(5, 2, [7, 7, 7, 7, 7])
        self.assertEqual(result, "ДА")

    def test_should_print_with_large_input(self):
        # Проверка на больших данных
        result = can_sort(10 ** 5, 2, list(range(10 ** 5, 0, -1)))
        self.assertEqual(result, "НЕТ")


if __name__ == '__main__':
    unittest.main()
