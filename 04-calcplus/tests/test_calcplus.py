from UnitTestUtils import UnitTestUtils
import unittest
import os
from pathlib import Path

class TestCalcplus(unittest.TestCase):

    def setUp(self):
        self.utils = UnitTestUtils(self, __file__, "../calcplus.py")

    def test_calculations(self):

        subtests = [
            ( ['5','6','+'],            '5 + 6 = 11', 'integer addition' ),
            ( ['10','2','/'],           '10 / 2 = 5', 'integer division with integer result' ),
            ( ['5','6','x'],            '5 x 6 = 30', 'integer multiplication' ),
            ( ['1.1','.2','-'],         '1.1 - 0.2 = 0.9', 'float subtraction' ),
            ( ['3.0','2.0','+'],        '3 + 2 = 5', 'float input shown as integer' ),
            ( ['-4','3','x'],           '-4 x 3 = -12', 'negative first number' ),
            ( ['8','-10','+'],          '8 + -10 = -2', 'negative second number' ),
            ( ['-6.6','-3','/'],        '-6.6 / -3 = 2.2', 'negative floats' ),
            ( ['4','3','/'],            '4 / 3 = 1.3333', 'integer division with float result' ),
            ( ['4','0','x'],            '4 x 0 = 0', 'multiply by 0' ),
            ( ['4','0','/'],            '4 / 0 = ERROR', 'divide by 0' ),
            ( ['2.02468','2.00000','/'],'2.02468 / 2 = 1.0123', 'both input and result require rounding' ),
            ( ['4','3','^'],            '4 ^ 3 = 64', 'int base, int expon' ),
            ( ['4.5','3','^'],          '4.5 ^ 3 = 91.125', 'float base, int expon' ),
            ( ['16','.5','^'],          '16 ^ 0.5 = 4', 'int base, float expon' ),
            ( ['-5','3','^'],           '-5 ^ 3 = -125', 'negative base, positive expon' ),
            ( ['2','-2','^'],           '2 ^ -2 = 0.25', 'positive base, negative expon' ),
            ( ['123','123','^'],        '123 ^ 123 = 1.1437436793461719e+257', 'pow uses scientific notation' ),
            ( ['123','456','^'],        '123 ^ 456 = ERROR', 'pow too big' ),
            ( ['two','',''],            'INVALID NUMBER', 'invalid first number' ),
            ( ['10','two',''],          'INVALID NUMBER', 'invalid second number' ),
            ( ['','',''],               'INVALID NUMBER', 'missing first number' ),
            ( ['1','',''],              'INVALID NUMBER', 'missing second number' ),
            ( ['3.5','2.0','*'],        'INVALID OPERATOR', 'invalid operator' ),
            ( ['1','1',''],             'INVALID OPERATOR', 'missing operator' ),
        ]

        for test in subtests:
            inputs = test[0]
            expected = test[1]
            description = test[2]
            with self.subTest(description):
                self.utils.check_one_equals(inputs, expected)

if __name__ == '__main__':
    unittest.main()
