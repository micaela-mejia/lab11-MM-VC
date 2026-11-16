# https://github.com/micaela-mejia/lab11-MM-VC
# Partner 1: Micaela Mejia
# Partner 2: Victor Corona

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -10),-15)
    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(-5, -10),5)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5.0)
        self.assertEqual(div(2, -10), -5.0)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(3, 81), 4)
        self.assertEqual(logarithm(2, 2), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2, 8)
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-4)
        # Test basic function
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()