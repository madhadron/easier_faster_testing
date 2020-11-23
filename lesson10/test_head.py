import unittest
import random
import sys
from head import head
from typing import List

def randlist(n: int) -> List[int]:
    return [random.randint(-sys.maxsize, sys.maxsize)
            for _ in range(n)]

class TestHead(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            head([])

    def test_head(self):
        cases = [
            randlist(1),
            randlist(2),
            randlist(6),
            randlist(35),
        ]
        for input in cases:
            with self.subTest(input=input):
                found = head(input)
                expected = input[0]
                self.assertEqual(expected, found)