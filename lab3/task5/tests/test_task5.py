import unittest
from lab3.task5.src.task5 import h_index



class TestHIndexFunction(unittest.TestCase):

    def test_should_h_index(self):
        # Тестирование работы функции h_index
        citations_1 = [6, 5, 3, 1, 0]
        citations_2 = [10, 8, 5, 4, 3]
        citations_3 = [1, 2, 3, 4, 5]
        citations_4 = [5, 5, 5, 5, 5]

        # Проверяем результаты работы функции
        self.assertEqual(h_index(citations_1), 3)
        self.assertEqual(h_index(citations_2), 4)
        self.assertEqual(h_index(citations_3), 3)
        self.assertEqual(h_index(citations_4), 5)


if __name__ == '__main__':
    unittest.main()
