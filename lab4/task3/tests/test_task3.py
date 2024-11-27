import unittest

from lab4.task3.src.task3 import *

class TestBracketSequence(unittest.TestCase):

    def test_empty_sequence(self):
        """Тест пустой строки"""
        # given
        sequence = ""

        # when
        result = is_valid_bracket_sequence(sequence)

        # then
        self.assertTrue(result)

    def test_single_type_brackets(self):
        """Тест последовательностей с одним типом скобок"""
        # given
        sequence_1 = "()"
        sequence_2 = "(())"
        sequence_3 = "(()"
        sequence_4 = "())"

        # when
        result_1 = is_valid_bracket_sequence(sequence_1)
        result_2 = is_valid_bracket_sequence(sequence_2)
        result_3 = is_valid_bracket_sequence(sequence_3)
        result_4 = is_valid_bracket_sequence(sequence_4)

        # then
        self.assertTrue(result_1)
        self.assertTrue(result_2)
        self.assertFalse(result_3)
        self.assertFalse(result_4)

    def test_mixed_brackets(self):
        """Тест смешанных типов скобок"""
        # given
        sequence_1 = "()[]"
        sequence_2 = "([])"
        sequence_3 = "([)]"
        sequence_4 = "[(])"

        # when
        result_1 = is_valid_bracket_sequence(sequence_1)
        result_2 = is_valid_bracket_sequence(sequence_2)
        result_3 = is_valid_bracket_sequence(sequence_3)
        result_4 = is_valid_bracket_sequence(sequence_4)

        # then
        self.assertTrue(result_1)
        self.assertTrue(result_2)
        self.assertFalse(result_3)
        self.assertFalse(result_4)

    def test_nested_brackets(self):
        """Тест вложенных скобок"""
        # given
        sequence_1 = "(([]))"
        sequence_2 = "[([])]"
        sequence_3 = "(([])"
        sequence_4 = "(([])))"

        # when
        result_1 = is_valid_bracket_sequence(sequence_1)
        result_2 = is_valid_bracket_sequence(sequence_2)
        result_3 = is_valid_bracket_sequence(sequence_3)
        result_4 = is_valid_bracket_sequence(sequence_4)

        # then
        self.assertTrue(result_1)
        self.assertTrue(result_2)
        self.assertFalse(result_3)
        self.assertFalse(result_4)

    def test_unbalanced_brackets(self):
        """Тест несбалансированных скобок"""
        # given
        sequence_1 = "("
        sequence_2 = ")"
        sequence_3 = "["
        sequence_4 = "]"

        # when
        result_1 = is_valid_bracket_sequence(sequence_1)
        result_2 = is_valid_bracket_sequence(sequence_2)
        result_3 = is_valid_bracket_sequence(sequence_3)
        result_4 = is_valid_bracket_sequence(sequence_4)

        # then
        self.assertFalse(result_1)
        self.assertFalse(result_2)
        self.assertFalse(result_3)
        self.assertFalse(result_4)

    def test_large_sequence(self):
        """Тест больших последовательностей"""
        # given
        sequence_1 = "()" * 5000
        sequence_2 = "(" * 5000 + ")" * 4999

        # when
        result_1 = is_valid_bracket_sequence(sequence_1)
        result_2 = is_valid_bracket_sequence(sequence_2)

        # then
        self.assertTrue(result_1)
        self.assertFalse(result_2)


if __name__ == "__main__":
    unittest.main()
