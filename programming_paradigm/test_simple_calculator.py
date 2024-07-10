import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtraction(self):
        """"Test the subtraction method."""
        self.assertEqual(self.calc.subtract(1, 5), -4)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1, 1), 0)

    def test_multiplication(self):
        """"Test the multiplication method"""
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(2, -2), -4)

    def test_division(self):
        """"Test the division method"""
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(-20, 2), -10)
        self.assertIsNone(self.calc.divide(2, 0), None)
