import unittest
from UnitTestUtils import UnitTestUtils

class TestLeapYear(unittest.TestCase):

    def setUp(self):
        self.utils = UnitTestUtils(self, __file__, "../leapify.py")

    def test_leap_years(self):

        subtests = [
            ( ['2020'], '2020 is a leap year',      'is divisible by 4' ),
            ( ['2024'], '2024 is a leap year',      'is divisible by 4' ),
            ( ['2021'], '2021 is not a leap year',  'is not divisible by 4' ),
            ( ['2022'], '2022 is not a leap year',  'is not divisible by 4' ),
            ( ['2023'], '2023 is not a leap year',  'is not divisible by 4' ),
            ( ['1800'], '1800 is not a leap year',  'is divisible by 100 but not 400' ),
            ( ['1900'], '1900 is not a leap year',  'is divisible by 100 but not 400' ),
            ( ['1600'], '1600 is a leap year',      'is divisible by 400' ),
            ( ['2000'], '2000 is a leap year',      'is divisible by 400' ),
            ( ['0'],    'INVALID',                  'not greater than 0'),
            ( ['-100'], 'INVALID',                  'not greater than 0'),
            ( ['202.4'], 'INVALID',                  'not an integer'),
            ( ['abcd'], 'INVALID',                  'not a number'),
        ]

        for test in subtests:
            inputs = test[0]
            expected = test[1]
            description = test[2]
            with self.subTest(description):
                self.utils.check_one_contains(inputs, expected)

if __name__ == '__main__':
    unittest.main()
