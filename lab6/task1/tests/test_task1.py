import unittest
from lab6.task1.src.task1 import process_operations

class TestSetOperations(unittest.TestCase):

    def test_should_add_and_query(self):
        # given
        n = 3
        operations = ["A 1", "A 2", "? 1"]

        # when
        result = process_operations(n, operations)

        # then
        self.assertEqual(result, ["Y"])

    def test_should_add_duplicate_and_query(self):
        # given
        n = 4
        operations = ["A 1", "A 1", "A 2", "? 2"]

        # when
        result = process_operations(n, operations)

        # then
        self.assertEqual(result, ["Y"])

    def test_should_make_query_nonexistent(self):
        # given
        n = 2
        operations = ["A 1", "? 3"]

        # when
        result = process_operations(n, operations)

        # then
        self.assertEqual(result, ["N"])

    def test_should_delete_and_query(self):
        # given
        n = 4
        operations = ["A 1", "D 1", "? 1", "? 2"]

        # when
        result = process_operations(n, operations)

        # then
        self.assertEqual(result, ["N", "N"])

    def test_should_delete_nonexistent(self):
        # given
        n = 3
        operations = ["A 1", "D 2", "? 1"]

        # when
        result = process_operations(n, operations)

        # then
        self.assertEqual(result, ["Y"])

if __name__ == "__main__":
    unittest.main()
