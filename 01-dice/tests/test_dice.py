import unittest
from unittest.mock import patch
from UnitTestUtils import UnitTestUtils

class TestDiceRoll(unittest.TestCase):

    def setUp(self):
        self.utils = UnitTestUtils(self, __file__, "../dice.py")

    @patch('random.randint', return_value=5)
    def test_valid_input_with_modifier(self, mock_random):
        self.utils.check_one_regex(
            ['6', '2'],
            r'5\s*\+\s*2\s*\=\s*7',
            "ROLL: 5 + 2 = 7"
        )
        mock_random.assert_called_with(1, 6)

    @patch('random.randint', return_value=3)
    def test_valid_input_no_modifier(self, mock_random):
        self.utils.check_one_regex(
            ['8', '0'],
            r'3',
            "ROLL: 3"
        )
        mock_random.assert_called_with(1, 8)

    @patch('random.randint', return_value=6)
    def test_valid_input_negative_modifier(self, mock_random):
        self.utils.check_one_regex(
            ['8', '-4'],
            r'6\s*\+\s*-4\s*\=\s*2',
            "ROLL: 6 + -4 = 2"
        )
        mock_random.assert_called_with(1, 8)

    @patch('random.randint', return_value=3)
    def test_valid_input_negative_modifier_edge(self, mock_random):
        self.utils.check_one_regex(
            ['4', '-1'],
            r'3\s*\+\s*-1\s*\=\s*2',
            "ROLL: 3 + -1 = 2"
        )
        mock_random.assert_called_with(1, 4)

    @patch('random.randint', return_value=2)
    def test_valid_input_negative_result(self, mock_random):
        self.utils.check_one_regex(
            ['12', '-4'],
            r'2\s*\+\s*-4\s*\=\s*0',
            "ROLL: 2 + -4 = 0"
        )
        mock_random.assert_called_with(1, 12)

    def test_invalid_sides_below_minimum(self):
        self.utils.check_one_contains(
            ['3','3'],
            'MUST ENTER 4 OR MORE SIDES'
        )

    def test_invalid_input_non_numeric_sides(self):
        self.utils.check_one_contains(
            ['bogus sides', '2'],
            'MUST ENTER A NUMBER'
        )

    def test_invalid_input_non_numeric_modifier(self):
        self.utils.check_one_contains(
            ['5', 'bogus modifier'],
            'MUST ENTER A NUMBER'
        )

if __name__ == '__main__':
    unittest.main()
