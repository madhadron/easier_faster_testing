from abbrev_range import abbrev_range
import unittest

class TestAbbrevRange(unittest.TestCase):
    def test_abbrev_range(self):
        cases = [
            # First boundary
            (0, ''),
            (1, '1'),
            (2, '1 2'),
            # First bulk
            (8, '1 2 3 4 5 6 7 8'),
            # Second boundary
            (10, '1 2 3 4 5 6 7 8 9 10'),
            (11, '1 2 3 4 5 6 7 ... 11'),
            (12, '1 2 3 4 5 6 7 ... 12'),
            # Second bulk
            (35, '1 2 3 4 5 6 7 ... 35'),
            (1024, '1 2 3 4 5 6 ... 1024'),
            # Third boundary
            (10**12, '1 ... 1000000000000'),
            # Then overflows under test_overflow
        ]
        for (input, expected) in cases:
            with self.subTest(input=input):
                found = abbrev_range(input)
                self.assertEqual(expected, found)

    def test_overflow(self):
        inputs = [10**13, 10**14, 10**17, 10**28]
        for input in inputs:
            with self.subTest(input=input):
                with self.assertRaises(ValueError):
                    abbrev_range(input)
            