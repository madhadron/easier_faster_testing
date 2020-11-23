import unittest
import random

from factor import factor
from typing import List

PRIMES: List[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41] 
# ...obviously there are more primes, but we have to stop somewhere

def product(xs):
    p = 1
    for x in xs:
        p *= x
    return p

class TestFactor(unittest.TestCase):
    def test_factor(self):
        for k in range(5):
            for _ in range(500):
                expected = sorted(random.choices(PRIMES, k=k))
                N = product(expected)
                with self.subTest(N=N, expected=expected):
                    found = sorted(factor(N))
                    self.assertEqual(expected, found)