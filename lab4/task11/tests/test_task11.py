import unittest
from lab4.task11.src.task11 import process_queue

class TestProcessQueue(unittest.TestCase):
    def test_should_work_when_all_documents_issued(self):
        # given
        n = 3
        m = 3
        a = [1, 1, 1]

        # when
        remaining_people, remaining_a = process_queue(n, m, a)

        # then
        self.assertEqual(remaining_people, -1)

    def test_should_work_when_some_documents_left(self):
        # given
        n = 3
        m = 2
        a = [1, 2, 3]

        # when
        remaining_people, remaining_a = process_queue(n, m, a)

        # then
        self.assertEqual(remaining_people, 2)
        self.assertEqual(remaining_a, [3, 1])

    def test_should_work_when_no_documents_to_issue(self):
        # given
        n = 3
        m = 0
        a = [1, 2, 3]

        # when
        remaining_people, remaining_a = process_queue(n, m, a)

        # then
        self.assertEqual(remaining_people, 3)
        self.assertEqual(remaining_a, [1, 2, 3])

    def test_should_work_when_single_person(self):
        # given
        n = 1
        m = 5
        a = [7]

        # when
        remaining_people, remaining_a = process_queue(n, m, a)

        # then
        self.assertEqual(remaining_people, 1)
        self.assertEqual(remaining_a, [2])

if __name__ == "__main__":
    unittest.main()
