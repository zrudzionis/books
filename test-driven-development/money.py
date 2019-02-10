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
-----------> Dollar/Franc duplication
    Common equals
    Common times
    Compare Francs with Dollars
    Currency?
Delete test_franc_multiplication?
"""

from unittest import TestCase


class Money(object):
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

    def currency(self):
        return self.currency_code

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency_code)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class MoneyTestCase(TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(five.times(2), Money.dollar(10))
        self.assertEqual(five.times(3), Money.dollar(15))

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertEqual(five.times(2), Money.franc(10))
        self.assertEqual(five.times(3), Money.franc(15))

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_currency(self):
        self.assertEqual(Money.dollar(1).currency(), 'USD')
        self.assertEqual(Money.franc(1).currency(), 'CHF')
