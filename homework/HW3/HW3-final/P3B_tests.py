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
        print('Error:', e)


# Test for withdrawing and depositing a negative amount
def test_negative_amount():
    user = bank.BankUser("Joe")
    user.addAccount(bank.AccountType.SAVINGS)
    user.deposit(bank.AccountType.SAVINGS, 10)
    try:
        user.withdraw(bank.AccountType.SAVINGS, -10)
    except Exception as e:
        print('Error:', e)
    try:
        user.deposit(bank.AccountType.SAVINGS, -10)
    except Exception as e:
        print('Error:', e)


# Test for duplicate attempts to create a savings and checking account
def test_duplicate_accounts():
    user = bank.BankUser("Joe")
    user.addAccount(bank.AccountType.SAVINGS)
    user.addAccount(bank.AccountType.CHECKING)
    try:
        user.addAccount(bank.AccountType.SAVINGS)
    except Exception as e:
        print('Error:', e)
    try:
        user.addAccount(bank.AccountType.CHECKING)
    except Exception as e:
        print('Error:', e)


# Test for if account doesn't exist for balance requests, withdrawing, and depositing
def test_account_exists():
    user = bank.BankUser("Joe")
    try:
        user.getBalance(bank.AccountType.SAVINGS)
    except Exception as e:
        print('Error:', e)
    try:
        user.deposit(bank.AccountType.CHECKING, 10)
    except Exception as e:
        print('Error:', e)
    try:
        user.withdraw(bank.AccountType.CHECKING, 10)
    except Exception as e:
        print('Error:', e)


# Call all tests
test_over_withdrawal()
test_negative_amount()
test_duplicate_accounts()
test_account_exists()
