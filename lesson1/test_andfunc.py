import unittest
from andfunc import _and

class TestAnd(unittest.TestCase):
    def test_and(self):
        cases = [
            ((True, True), True),
            ((True, False), False),
            ((False, True), False),
            ((False, False), False),
        ]
        for (input, expected) in cases:
            with self.subTest(input=input):
                found = _and(input[0], input[1])
                self.assertEqual(expected, found)