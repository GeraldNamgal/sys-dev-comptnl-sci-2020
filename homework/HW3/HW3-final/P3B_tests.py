#!/usr/bin/env python3

import bank.Bank as bank


# Test for trying to withdraw more than balance
def test_over_withdrawal():
    user = bank.BankUser("Joe")
    user.addAccount(bank.AccountType.SAVINGS)
    user.deposit(bank.AccountType.SAVINGS, 10)
    try:
        user.withdraw(bank.AccountType.SAVINGS, 1000)
    except Exception as e:
        print('Error message:', e)


# Test for withdrawing and depositing a negative amount
def test_negative_amount():
    user = bank.BankUser("Joe")
    user.addAccount(bank.AccountType.SAVINGS)
    user.deposit(bank.AccountType.SAVINGS, 10)
    try:
        user.withdraw(bank.AccountType.SAVINGS, -10)
    except Exception as e:
        print('Error message:', e)
    try:
        user.deposit(bank.AccountType.SAVINGS, -10)
    except Exception as e:
        print('Error message:', e)


test_over_withdrawal()
test_negative_amount()
