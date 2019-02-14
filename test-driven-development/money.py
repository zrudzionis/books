"""
$5 + 10 CHF = $10 if rate is 2:1
------------> $5 + $5 = $10
Return Money from $5 + $5
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

    def plus(self, addend):
        return Sum(self, addend)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class Expression(object):
    pass


class Sum(object):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend


class Bank(object):
    def reduce(self, expression, currency_code):
        return Money.dollar(10)


class MoneyTestCase(TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(five.times(2), Money.dollar(10))
        self.assertEqual(five.times(3), Money.dollar(15))

    def test_equality(self):
        self.assertTrue(Money.dollar(5) == Money.dollar(5))
        self.assertFalse(Money.dollar(5) == Money.dollar(6))
        self.assertFalse(Money.dollar(5) == Money.franc(5))

    def test_currency(self):
        self.assertEqual(Money.dollar(1).currency(), 'USD')
        self.assertEqual(Money.franc(1).currency(), 'CHF')

    def test_simple_addition(self):
        five = Money.dollar(5)
        s = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(s, 'USD')
        self.assertEqual(reduced, Money.dollar(10))

    def test_plus_returns_sum(self):
        five = Money.dollar(5)
        s = five.plus(five)
        self.assertEqual(s.augend, five)
        self.assertEqual(s.addend, five)
