import unittest

from lab6.task2.src.task2 import *
class TestPhoneBookManager(unittest.TestCase):

    # Тест на номер, начинающийся с нуля
    def test_should_react_when_add_number_with_leading_zero(self):
        # given
        given = [
            "add 0123456 Alice"
        ]

        # when
        when = process_phone_book(given)

        # then
        then = ["invalid"]
        self.assertEqual(when, then)

    # Тест на имя длиной более 15 символов
    def test_should_react_when_add_name_too_long(self):
        # given
        given = [
            "add 1234567 ThisNameIsWayTooLong"
        ]

        # when
        when = process_phone_book(given)

        # then
        then = ["invalid"]
        self.assertEqual(when, then)

    # Тест на добавление и поиск существующего номера
    def test_should_find_existing_number(self):
        # given
        given = [
            "add 1234567 John",
            "find 1234567"
        ]

        # when
        when = process_phone_book(given)

        # then
        then = ["John"]
        self.assertEqual(when, then)

    # Тест на поиск несуществующего номера
    def test_should_find_non_existing_number(self):
        # given
        given = [
            "find 7654321"
        ]

        # when
        when = process_phone_book(given)

        # then
        then = ["not found"]
        self.assertEqual(when, then)

    # Тест на удаление существующего номера и поиск
    def test_should_delete_existing_number(self):
        # given
        given = [
            "add 1234567 John",
            "del 1234567",
            "find 1234567"
        ]

        # when
        when = process_phone_book(given)

        # then
        then = ["not found"]
        self.assertEqual(when, then)

    # Тест на удаление несуществующего номера
    def test_should_delete_non_existing_number(self):
        # given
        given = [
            "del 7654321"
        ]

        # when
        when = process_phone_book(given)

        # then
        then = []
        self.assertEqual(when, then)

    # Тест на несколько запросов
    def test_should_work_with_multiple_queries(self):
        # given
        given = [
            "add 1234567 John",
            "add 7654321 Alice",
            "find 1234567",
            "find 7654321",
            "find 1111111"
        ]

        # when
        when = process_phone_book(given)

        # then
        then = ["John", "Alice", "not found"]
        self.assertEqual(when, then)


if __name__ == "__main__":
    unittest.main()
