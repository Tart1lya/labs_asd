import unittest
from lab4.task8.src.task8 import evaluate_postfix

class TestEvaluatePostfix(unittest.TestCase):
    def test_should_work_with_basic_operations(self):
        # given
        expressions = [
            (["2", "3", "+"], 5),
            (["10", "4", "-"], 6),
            (["6", "7", "*"], 42),
        ]

        # when-then
        for expr, expected in expressions:
            with self.subTest(expr=expr):
                self.assertEqual(evaluate_postfix(expr), expected)

    def test_should_work_with_complex_expression(self):
        # given
        expression = ["2", "3", "+", "4", "*", "5", "+"]

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, 25)

    def test_should_work_with_large_numbers(self):
        # given
        expression = ["2147483646", "1", "+"]

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, 2147483647)

    def test_should_work_with_invalid_operator(self):
        # given
        expression = ["2", "3", "&"]

        # when-then
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(expression)

        self.assertIn("Неизвестный оператор", str(context.exception))

    def test_should_work_with_intermediate_overflow(self):
        # given
        expression = ["1073741824", "2", "*"]

        # when-then
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(expression)

        self.assertIn("Промежуточный результат превышает предел", str(context.exception))

    def test_should_work_with_number_out_of_bounds(self):
        # given
        expression = ["2147483648"]

        # when-then
        with self.assertRaises(ValueError) as context:
            evaluate_postfix(expression)

        self.assertIn("выходящее за пределы", str(context.exception))

    def test_should_work_with_empty_expression(self):
        # given
        expression = []

        # when-then
        with self.assertRaises(IndexError):
            evaluate_postfix(expression)

    def test_should_work_with_unbalanced_expression(self):
        # given
        expression = ["2", "+"]

        # when-then
        with self.assertRaises(IndexError):
            evaluate_postfix(expression)

    def test_should_valid_with_zeros(self):
        # given
        expression = ["0", "0", "+", "0", "*"]

        # when
        result = evaluate_postfix(expression)

        # then
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
