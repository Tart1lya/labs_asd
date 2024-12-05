import unittest
from lab7.task7.src.task7 import matches_pattern  # Предполагается, что основной код находится в файле task.py

class TestMatchesPattern(unittest.TestCase):

    def test_should_work_when_exact_match(self):
        # given
        pattern = "kitten"
        string = "kitten"

        # when
        result = matches_pattern(pattern, string)

        # then
        self.assertEqual(result, "YES")

    def test_should_work_with_question_mark(self):
        # given
        pattern = "k?tten"
        string = "kitten"

        # when
        result = matches_pattern(pattern, string)

        # then
        self.assertEqual(result, "YES")

    def test_should_work_with_asterisk(self):
        # given
        pattern = "*ten"
        string = "kitten"

        # when
        result = matches_pattern(pattern, string)

        # then
        self.assertEqual(result, "YES")

    def test_should_work_when_no_match(self):
        # given
        pattern = "dog"
        string = "cat"

        # when
        result = matches_pattern(pattern, string)

        # then
        self.assertEqual(result, "NO")

    def test_should_work_when_asterisk_and_question_mark(self):
        # given
        pattern = "*a?b"
        string = "zaab"

        # when
        result = matches_pattern(pattern, string)

        # then
        self.assertEqual(result, "YES")

    def test_should_work_with_empty_pattern(self):
        # given
        pattern = ""
        string = "kitten"

        # when
        result = matches_pattern(pattern, string)

        # then
        self.assertEqual(result, "NO")

    def test_should_work_when_empty_string(self):
        # given
        pattern = "*"
        string = ""

        # when
        result = matches_pattern(pattern, string)

        # then
        self.assertEqual(result, "YES")

    def test_should_work_when_empty_pattern_and_string(self):
        # given
        pattern = ""
        string = ""

        # when
        result = matches_pattern(pattern, string)

        # then
        self.assertEqual(result, "YES")

if __name__ == "__main__":
    unittest.main()
