import unittest
import math
from calculator import (
    add, sub, mul, div, mod,
    power, sqrt, sin, cos,
    floor, ceil
)

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 5), -5)

    def test_mul(self):
        self.assertEqual(mul(4, 3), 12)
        self.assertEqual(mul(-2, 3), -6)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_mod(self):
        self.assertEqual(mod(10, 3), 1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3)

    def test_trigonometry(self):
        self.assertAlmostEqual(sin(math.pi / 2), 1, places=5)
        self.assertAlmostEqual(cos(0), 1, places=5)

    def test_rounding(self):
        self.assertEqual(floor(3.7), 3)
        self.assertEqual(ceil(3.2), 4)

if __name__ == "__main__":
    unittest.main()
