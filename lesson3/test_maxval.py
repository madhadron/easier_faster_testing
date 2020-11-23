import unittest
from maxval import maxval
from math import inf

class TestHead(unittest.TestCase):
    # Boundary:
    #   {} → -inf
    #   {'a': 1} → 1
    #   {'a': 1, 'b': 1} → 1
    #   {'a': 1, 'b': 2} → 2
    # Bulk:
    #   {'a': 5, 'b': 12, 'c': 42, 'd': 961, 'e': 128} → 961
    #   {'boris': 400, 'blah': 999, 'quirk': 421} → 999
    def test_head(self):
        cases = [
            ({}, -inf),
            ({'a': 1}, 1),
            ({'a': 1, 'b': 1}, 1),
            ({'a': 1, 'b': 2}, 2),
            ({'a': 5, 'b': 12, 'c': 42, 'd': 961, 'e': 128}, 961),
            ({'boris': 400, 'blah': 999, 'quirk': 421}, 999),
        ]
        for input, expected in cases:
            with self.subTest(input=input):
                found = maxval(input)
                self.assertEqual(expected, found)