import unittest
import random

from factor import factor
from typing import List

PRIMES: List[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, ...]

def product(xs):
    p = 1
    for x in xs:
        p *= x
    return p

class TestFactor(unittest.TestCase):
    def test_product_factor_is_identity(self):
        for k in range(5):
            for _ in range(500):
                N = random.randint(1, 10**5)
                with self.subTest(N=N):
                    self.assertEqual(N, product(factor(N)))

    def factor_product_is_identity(self):
        for k in range(5):
            for _ in range(500):
                primes = sorted(random.choices(PRIMES, k=N))
                with self.subTest(primes=primes):
                    self.assertEqual(primes, factor(product(primes)))