import unittest
from lab5.task6.src.task6 import *

class TestProcessPriorityQueue(unittest.TestCase):
    def test_should_add_and_extract_minimal(self):
        # given
        operations = ["A 5", "A 3", "A 7", "X", "X", "X"]

        # when
        result = process_priority_queue(operations)

        # then
        self.assertEqual(result, ["3", "5", "7"])

    def test_should_extract_from_empty(self):
        # given
        operations = ["X", "X"]

        # when
        result = process_priority_queue(operations)

        # then
        self.assertEqual(result, ["*", "*"])

    def test_should_decrease_key(self):
        # given
        operations = ["A 10", "A 15", "A 20", "D 1 5", "X", "X", "X"]

        # when
        result = process_priority_queue(operations)

        # then
        self.assertEqual(result, ["5", "10", "20"])


    def test_should_work_with_large_numbers(self):
        # given
        operations = ["A 1000000000", "A -1000000000", "X", "X", "X"]

        # when
        result = process_priority_queue(operations)

        # then
        self.assertEqual(result, ["-1000000000", "1000000000", "*"])


if __name__ == "__main__":
    unittest.main()
