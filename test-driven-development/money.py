"""
------------> $5 + 10 CHF = $10 if rate is 2:1
    $5 + $5 = $10
Return Money from $5 + $5
    Bank.reduce(Money)
    Reduce Money with conversion
    Reduce(Bank, String)
"""

from unittest import TestCase
from abc import abstractmethod


class Expression(object):
    @abstractmethod
    def reduce(self, bank, to_currency_code):
        raise NotImplementedError

    @abstractmethod
    def plus(self, addend):
        raise NotImplementedError


class Money(Expression):
    def __init__(self, amount, currency_code):
        self.amount = amount
        self.currency_code = currency_code

    def currency(self):
        return self.currency_code

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency_code)

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to_currency_code):
        rate = bank.rate(self.currency_code, to_currency_code)
        return Money(self.amount/rate, to_currency_code)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency_code == other.currency_code

    def __repr__(self):
        return 'Money(%s, %s)' % (self.amount, self.currency_code)

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, currency_code):
        augend = bank.reduce(self.augend, currency_code)
        addend = bank.reduce(self.addend, currency_code)
        amount = augend.amount + addend.amount
        return Money(amount, currency_code)

    def plus(self, addend):
        raise NotImplementedError


class Bank(object):
    def __init__(self):
        self.rates = dict()

    def reduce(self, expression, to_currency_code):
        return expression.reduce(self, to_currency_code)

    def rate(self, from_currency_code, to_currency_code):
        k = (from_currency_code, to_currency_code)
        return self.rates.get(k, 1)

    def add_rate(self, from_currency_code, to_currency_rate, rate):
        k = (from_currency_code, to_currency_rate)
        self.rates[k] = rate


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

    def test_reduce_sum(self):
        s = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(s, 'USD')
        self.assertEqual(result, Money.dollar(7))

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), 'USD')
        self.assertEqual(result, Money.dollar(1))

    def test_reduce_money_different_currencies(self):
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')
        self.assertEqual(result, Money.dollar(1))

    def test_identity_rate(self):
        bank = Bank()
        self.assertEqual(bank.rate('USD', 'USD'), 1)

    def test_mixed_addition(self):
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(five_bucks.plus(ten_francs), 'USD')
        self.assertEqual(Money.dollar(10), result)
