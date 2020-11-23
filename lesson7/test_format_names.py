from format_names import format_names
import unittest

class TestFormatNames(unittest.TestCase):
    def test_format_names(self):
        cases = [
            # First boundary, around the empty list
            ([], 'No one'),
            (['Jeff Y'], 'Jeff Y'),
            (['Jeff Y', 'Jane P'], 'Jeff Y and Jane P'),
            (
                ['Jeff Y', 'Jane P', 'Bill J'], 
                'Jeff Y, Jane P, and Bill J',
            ),
            (
                ['Jeff Y', 'Jane P', 'Bill J', 'Eddy Q'], 
                'Jeff Y, Jane P, and 2 others',
            ),
            # First bulk
            (
                ['Jeff Y', 'Jane P', 'Bill J', 'Eddy Q',
                 'Morris V', 'Edna M']*2, 
                'Jeff Y, Jane P, and 10 others',
            ),
            (
                ['Jeff Y', 'Jane P', 'Bill J', 'Eddy Q',
                 'Morris V', 'Edna M']*3, 
                'Jeff Y, Jane P, and 16 others',
            ),
            # Second boundary
            (
                ['Jeff Y', 'Jane P', 'Bill J', 
                 'Eddy Q', 'Morris V']*5,
                 'Jeff Y, Jane P, and 23 others'),
            (
                ['Jeff Y', 'Jane P', 'Bill J', 
                 'Eddy Q', 'Morris V']*5 + ['Adam S'],
                '26 people',
            ),
            # Second bulk
            (['Jeff Y', 'Jane P']*50, '100 people'),
            (['Jeff Y', 'Jane P']*500, '1000 people'),
        ]
        for (input, expected) in cases:
            with self.subTest(input=input):
                found = format_names(input)
                self.assertEqual(expected, found)