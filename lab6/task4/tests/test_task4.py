import unittest
from lab6.task4.src.task4 import process_commands


class TestProcessCommands(unittest.TestCase):
    def test_should_put_and_get(self):
        # given
        commands = ["put key1 value1", "put key2 value2", "get key1", "get key2", "get key3"]

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, ["value1", "value2", "<none>"])

    def test_should_put_overwrite(self):
        # given
        commands = ["put key1 value1", "put key1 value2", "get key1"]

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, ["value2"])

    def test_should_work_prev_and_next(self):
        # given
        commands = [
            "put key1 value1",
            "put key2 value2",
            "put key3 value3",
            "prev key2",
            "next key2",
            "prev key1",
            "next key3",
        ]

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, ["value1", "value3", "<none>", "<none>"])

    def test_should_delete(self):
        # given
        commands = ["put key1 value1", "put key2 value2", "delete key1", "get key1", "get key2"]

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, ["<none>", "value2"])

    def test_should_work_when_empty_commands(self):
        # given
        commands = []

        # when
        result = process_commands(commands)

        # then
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
