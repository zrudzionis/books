"""
$5 + 10 CHF = $10 if rate is 2:1
    $5 * 2 = $10
Make "amount" private
    Dollar side-effects?
Money rounding?
    equals()
hashCode()
"""

from unittest import TestCase


class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def __eq__(self, other):
        return self.amount == getattr(other, 'amount', None)


class MoneyTestCase(TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(product.amount, 10)
        product = five.times(3)
        self.assertEqual(product.amount, 15)

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertFalse(Dollar(5) == Dollar(6))
        self.assertFalse(Dollar(5) == dict())
