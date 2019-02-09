"""
$5 + 10 CHF = $10 if rate is 2:1
    $5 * 2 = $10
    Make "amount" private
    Dollar side-effects?
Money rounding?
    equals()
hashCode()
equal None
equal other object
5 CHF * 2 = 10 CHF
"""

from unittest import TestCase


class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == other.amount


class MoneyTestCase(TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        self.assertEqual(five.times(2), Dollar(10))
        self.assertEqual(five.times(3), Dollar(15))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(five.times(2), Franc(10))
        self.assertEqual(five.times(3), Franc(15))

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
