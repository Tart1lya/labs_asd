import unittest
from lab3.task6.src.task6 import generate_pairwise_array


class TestGeneratePairwiseArray(unittest.TestCase):

    def test_should_generate_pairwise_array(self):
        # given
        A = [1, 2]
        B = [3, 4]

        # when
        result = generate_pairwise_array(A, B)

        # then
        expected_output = [3, 4, 6, 8]
        self.assertEqual(result, expected_output)

    def test_should_work_with_empty_arrays(self):
        # given
        A = []
        B = []

        # when
        result = generate_pairwise_array(A, B)

        # then
        expected_output = []
        self.assertEqual(result, expected_output)

    def test_should_work_with_single_element_arrays(self):
        # given
        A = [5]
        B = [10]

        # when
        result = generate_pairwise_array(A, B)

        # then
        expected_output = [50]
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
