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
Dollar/Franc duplication
    Common equals
Common times
    Compare Francs with Dollars
-----------> Currency?
Delete test_franc_multiplication?
"""

from unittest import TestCase


class Money(object):
    def __init__(self, amount):
        self.amount = amount
        self.currency_code = None

    def __eq__(self, other):
        return self.amount == other.amount and self.__class__ == other.__class__

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


class Dollar(Money):
    def __init__(self, amount):
        super(Dollar, self).__init__(amount)
        self.currency_code = 'USD'

    def currency(self):
        return self.currency_code

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        super(Franc, self).__init__(amount)
        self.currency_code = 'CHF'

    def currency(self):
        return self.currency_code

    def times(self, multiplier):
        return Franc(self.amount * multiplier)


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
        self.assertTrue(Franc(5) == Franc(5))
        self.assertFalse(Franc(5) == Franc(6))
        self.assertFalse(Money.dollar(5) == Franc(5))

    def test_currency(self):
        self.assertEqual(Money.dollar(1).currency(), 'USD')
        self.assertEqual(Money.franc(1).currency(), 'CHF')
