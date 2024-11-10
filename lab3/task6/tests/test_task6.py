import unittest
from lab3.task6.src.task6 import generate_pairwise_array



class TestGeneratePairwiseArray(unittest.TestCase):

    def test_should_generate_pairwise_array(self):
        # Проверка на правильность формирования массива попарных произведений
        A = [1, 2]
        B = [3, 4]
        expected_output = [3, 4, 6, 8]
        self.assertEqual(generate_pairwise_array(A, B), expected_output)

    def test_should_work_with_empty_arrays(self):
        # Проверка на пустые массивы
        A = []
        B = []
        expected_output = []
        self.assertEqual(generate_pairwise_array(A, B), expected_output)

    def test_should_work_withsingle_element_arrays(self):
        # Проверка на случай массивов из одного элемента
        A = [5]
        B = [10]
        expected_output = [50]
        self.assertEqual(generate_pairwise_array(A, B), expected_output)

if __name__ == '__main__':
    unittest.main()
