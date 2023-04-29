from account import Account
import pytest


def test_init():
    acc = Account('John')
    assert acc.account_name() == 'John'
    assert acc.account_balance() == 0

def test_deposit():
    acc = Account('John')
    assert acc.deposit(100) == True
    assert acc.account_balance() == 100
    assert acc.deposit(-50) == False
    assert acc.account_balance() == 100

def test_withdraw():
    acc = Account('John')
    assert acc.deposit(100) == True
    assert acc.withdraw(50) == True
    assert acc.account_balance() == 50
    assert acc.withdraw(-50) == False
    assert acc.account_balance() == 50
    assert acc.withdraw(100) == False
    assert acc.account_balance() == 50
