
import unittest

from converter import UNITS, convert_units 


class TestUnitConverter(unittest.TestCase):

    def test_kilometers_to_miles(self):
        result = convert_units(5, "Kilometers (km)", "Miles (mi)")
        self.assertAlmostEqual(result, 3.106856, places=5)

    def test_kilograms_to_grams(self):
        result = convert_units(10, "Kilograms (kg)", "Grams (g)")
        self.assertEqual(result, 10000)

    def test_celsius_to_fahrenheit(self):
        result = convert_units(100, "Celsius (°C)", "Fahrenheit (°F)")
        self.assertAlmostEqual(result, 212)

    def test_liters_to_milliliters(self):
        result = convert_units(1, "Liters (L)", "Milliliters (mL)")
        self.assertEqual(result, 1000)

    def test_hours_to_minutes(self):
        result = convert_units(2, "Hours (h)", "Minutes (min)")
        self.assertEqual(result, 120)

    def test_same_unit(self):
        result = convert_units(5, "Meters (m)", "Meters (m)")
        self.assertEqual(result, 5)

    def test_incompatible_units(self):
        with self.assertRaises(ValueError):
            convert_units(5, "Meters (m)", "Kilograms (kg)")


if __name__ == "__main__":
    unittest.main()