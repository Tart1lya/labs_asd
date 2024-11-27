import unittest
from lab4.task1.src.task1 import process_stack


class TestStackProcessor(unittest.TestCase):

    def test_should_make_process_stack_with_simple(self):
        # given
        commands = ["+ 5", "-"]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, [5])

    def test_should_make_process_stack_with_multiple(self):
        # given
        commands = ["+ 1", "+ 10", "-", "+ 2", "+ 1234", "-"]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, [10, 1234])

    def test_should_make_process_stack_with_large(self):
        # given
        commands = ["+ 1000000000", "+ -1000000000", "-", "-"]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, [-1000000000, 1000000000])

    def test_should_make_process_stack_with_interleaved(self):
        # given
        commands = ["+ 7", "+ 14", "-", "+ 21", "+ 28", "-", "-"]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, [14, 28, 21])

    def test_should_make_process_stack_with_only_push(self):
        # given
        commands = ["+ 1", "+ 2", "+ 3"]

        # when
        result = process_stack(commands)

        # then
        self.assertEqual(result, [])
