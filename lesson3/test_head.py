import unittest
from head import head

class TestHead(unittest.TestCase):
    # Boundary:
    #   [] -> raises ValueError
    #   [522] -> 522
    #   [5, 2] -> 5
    # Bulk:
    #   [128, 53, 921, 1022, 41] -> 128
    #   [1, 5, 3, 12, 8, 1, 3, 2, 1, 5, 3, 19] -> 1
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            # head behaves quite differently on [],
            # so we can't lump it in with the other
            # cases without being ridiculously
            # complicated.
            head([])

    def test_head(self):
        cases = [
            ([522], 522),
            ([5, 2], 5),
            ([128, 53, 921, 1022, 41], 128),
            ([1, 5, 3, 12, 8, 1, 3, 2, 1, 5, 3, 19], 1),
        ]
        for input, expected in cases:
            with self.subTest(input=input):
                found = head(input)
                self.assertEqual(expected, found)