import unittest
from lab3.task7.src.task7 import radix_sort_phase



class TestRadixSort(unittest.TestCase):

    def test_should_make_radix_sort_phase(self):
        strings = [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ]

        # Сортировка по фазе 2 (индекс 2)
        sorted_strings = radix_sort_phase(strings, 2)
        self.assertEqual(sorted_strings, [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ])

        # Сортировка по фазе 1 (индекс 1)
        sorted_strings = radix_sort_phase(strings, 1)
        self.assertEqual(sorted_strings, [
            (1, "abc"),
            (2, "acd"),
            (3, "bcd")
        ])

if __name__ == '__main__':
    unittest.main()
