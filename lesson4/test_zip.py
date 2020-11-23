import unittest
from zip import zip

class TestZip(unittest.TestCase):
    def test_head(self):
        xs_cases = [
            [], [5], [3, 8], 
            [1, 12, 5, 32, 9, 1, 3, 17],
        ]
        ys_cases = [
            [], [''], ['a', 'b'], 
            ['vrrp', 'meep', 'baboon', 'trilobyte'],
        ]
        cases = [(xs, ys) for xs in xs_cases for ys in ys_cases]
        for xs, ys in cases:
            with self.subTest(xs=xs, ys=ys):
                found = zip(xs, ys)
                n = min(len(xs), len(ys))
                self.assertEqual([v[0] for v in found], xs[:n])
                self.assertEqual([v[1] for v in found], ys[:n])