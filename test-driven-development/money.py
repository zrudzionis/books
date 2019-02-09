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
"""

from unittest import TestCase


class Money(object):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount and self.__class__ == other.__class__


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


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
        self.assertTrue(Franc(5) == Franc(5))
        self.assertFalse(Franc(5) == Franc(6))
        self.assertFalse(Dollar(5) == Franc(5))
