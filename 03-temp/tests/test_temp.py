import unittest
from unittest.mock import patch
from UnitTestUtils import UnitTestUtils

alt_oregon_temps = [29.8, 32.6, 41.2, 52.0, 63.2, 72.1, 77.6, 76.4, 67.5, 55.0, 45.2, 33.8]
alt_maine_temps = [45.1, 48.2, 52.8, 58.9, 65.3, 72.4, 78.2, 77.1, 71.2, 60.3, 50.8, 45.5]


class TestTemperatureAnalysis(unittest.TestCase):

    def setUp(self):
        self.utils = UnitTestUtils(self, __file__, "../temp.py")

    def test_average_and_stability(self):
        expected_output = (
            "Oregon: 60.48 F, Variation: 12.20\n"
            "Maine: 53.87 F, Variation: 17.45\n"
            "Maine has the chilliest weather.\n"
            "Oregon has the most stable temperatures."
        )
        self.utils.check_one_equals([], expected_output)

    @patch('states.oregon_temps', alt_oregon_temps)
    @patch('states.maine_temps', alt_maine_temps)
    def test_alt_average_and_stability(self):
        expected_output = (
            "Oregon: 53.87 F, Variation: 17.45\n"
            "Maine: 60.48 F, Variation: 12.20\n"
            "Oregon has the chilliest weather.\n"
            "Maine has the most stable temperatures."
        )
        self.utils.check_one_equals([], expected_output)


if __name__ == '__main__':
    unittest.main()
