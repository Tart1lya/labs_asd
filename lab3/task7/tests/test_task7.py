import unittest
from lab3.task7.src.task7 import radix_sort_phase


class TestRadixSort(unittest.TestCase):

    def test_should_make_radix_sort_phase(self):
        # given
        strings = [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ]

        # when
        sorted_strings_phase_2 = radix_sort_phase(strings, 2)

        # then
        self.assertEqual(sorted_strings_phase_2, [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ])

        # when
        sorted_strings_phase_1 = radix_sort_phase(strings, 1)

        # then
        self.assertEqual(sorted_strings_phase_1, [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ])


if __name__ == '__main__':
    unittest.main()
