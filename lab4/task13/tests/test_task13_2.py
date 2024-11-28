import unittest
from lab4.task13.src.task13_2 import *

class TestQueue(unittest.TestCase):

    def test_enqueue_and_dequeue(self):
        # given
        queue = Queue(max_size=3)

        # when
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        # then
        self.assertEqual(queue.peek(), 10)  # Проверка первого элемента

        # when
        dequeued_value = queue.dequeue()

        # then
        self.assertEqual(dequeued_value, 10)  # Проверка удалённого элемента
        self.assertEqual(queue.peek(), 20)  # Проверка первого элемента после удаления

    def test_enqueue_when_full(self):
        # given
        queue = Queue(max_size=3)

        # when
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        # then
        with self.assertRaises(OverflowError):  # Проверка переполнения
            queue.enqueue(40)

    def test_dequeue_when_empty(self):
        # given
        queue = Queue(max_size=3)

        # when
        with self.assertRaises(IndexError):  # Проверка на удаление из пустой очереди
            queue.dequeue()

    def test_peek_when_empty(self):
        # given
        queue = Queue(max_size=3)

        # when
        with self.assertRaises(IndexError):  # Проверка на просмотр пустой очереди
            queue.peek()

    def test_is_empty(self):
        # given
        queue = Queue(max_size=3)

        # when
        queue.enqueue(10)

        # then
        self.assertFalse(queue.is_empty())  # Проверка, что очередь не пуста после добавления элемента

        # when
        queue.dequeue()

        # then
        self.assertTrue(queue.is_empty())  # Проверка, что очередь пуста после удаления элемента

    def test_is_full(self):
        # given
        queue = Queue(max_size=3)

        # when
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        # then
        self.assertTrue(queue.is_full())  # Проверка, что очередь полна

        # when
        queue.dequeue()

        # then
        self.assertFalse(queue.is_full())  # Проверка, что очередь не полна после удаления элемента


if __name__ == '__main__':
    unittest.main()
