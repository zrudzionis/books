"""
$5 + 10 CHF = $10 if rate is 2:1
    $5 * 2 = $10
Make "amount" private
    Dollar side-effects?
Money rounding?
"""

from unittest import TestCase


class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class MoneyTestCase(TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(product.amount, 10)
        product = five.times(3)
        self.assertEqual(product.amount, 15)
