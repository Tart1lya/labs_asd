import unittest
from lab4.task5.src.task5 import MaxStack  # Импортируем класс из файла решения


class TestMaxStack(unittest.TestCase):

    def test_push_and_max(self):
        # given
        max_stack = MaxStack()

        # when
        max_stack.push(2)

        # then
        self.assertEqual(max_stack.max(), 2)

        # when
        max_stack.push(1)

        # then
        self.assertEqual(max_stack.max(), 2)

        # when
        max_stack.push(3)

        # then
        self.assertEqual(max_stack.max(), 3)

    def test_pop(self):
        # given
        max_stack = MaxStack()
        max_stack.push(5)
        max_stack.push(3)
        max_stack.push(7)

        # when
        max_stack.pop()

        # then
        self.assertEqual(max_stack.max(), 5)

        # when
        max_stack.pop()

        # then
        self.assertEqual(max_stack.max(), 5)

        # when
        max_stack.pop()

        # then
        self.assertIsNone(max_stack.max())

    def test_empty_stack_max(self):
        # given
        max_stack = MaxStack()

        # when
        result = max_stack.max()

        # then
        self.assertIsNone(result)

    def test_push_pop_push(self):
        # given
        max_stack = MaxStack()

        # when
        max_stack.push(10)
        max_stack.pop()
        max_stack.push(20)

        # then
        self.assertEqual(max_stack.max(), 20)

    def test_push_same_values(self):
        # given
        max_stack = MaxStack()

        # when
        max_stack.push(5)
        max_stack.push(5)
        max_stack.push(5)

        # then
        self.assertEqual(max_stack.max(), 5)

        # when
        max_stack.pop()

        # then
        self.assertEqual(max_stack.max(), 5)

        # when
        max_stack.pop()

        # then
        self.assertEqual(max_stack.max(), 5)

        # when
        max_stack.pop()

        # then
        self.assertIsNone(max_stack.max())


if __name__ == '__main__':
    unittest.main()
