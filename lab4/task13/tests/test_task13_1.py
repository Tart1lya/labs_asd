import unittest
from lab4.task13.src.task13_1 import *


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()  # Новый стек для каждого теста

    def test_should_work_isEmpty_when_stack_is_empty(self):
        # given:

        # when:
        self.assertTrue(self.stack.isEmpty())

        # then:
        pass

    def test_should_work_isEmpty_when_stack_is_not_empty(self):
        # given:
        self.stack.push(10)

        # when:
        self.assertFalse(self.stack.isEmpty())

        # then:
        pass

    def test_should_work_push_and_pop(self):
        # given:
        self.stack.push(10)
        self.stack.push(20)

        # when:
        popped = self.stack.pop()

        # then:
        self.assertEqual(popped, 20)
        self.assertFalse(self.stack.isEmpty())

        popped = self.stack.pop()
        self.assertEqual(popped, 10)

        # then:
        self.assertTrue(self.stack.isEmpty())

    def test_should_work_pop_when_empty_stack(self):
        # given:

        # when:
        popped = self.stack.pop()

        # then:
        self.assertIsNone(popped)


if __name__ == '__main__':
    unittest.main()
