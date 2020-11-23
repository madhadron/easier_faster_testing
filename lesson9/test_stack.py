from stack import Stack
import unittest

def push(v):
    return ('push', [v])

def pop():
    return ('pop', [])

class TestStack(unittest.TestCase):
    def test_head(self):
        cases = [
            ([push(5)], 5),
            ([push(5), pop(), push(3)], 3),
            ([push(5), push(3), pop(), push(12), 
              push(8), pop(), pop(), push(9)], 9),
        ]
        for (input, expected) in cases:
            with self.subTest(input=input):
                st = Stack()
                for (f, args) in input:
                    getattr(st, f)(*args)
                found = st.head()
                self.assertEqual(expected, found)

    def test_head_empty(self):
        cases = [
            [],
            [push(5), pop(), pop()],
            [pop()],
        ]
        for input in cases:
            with self.subTest(input=input):
                st = Stack()
                with self.assertRaises(IndexError):
                    for (f, args) in input:
                        getattr(st, f)(*args)
                    st.head()