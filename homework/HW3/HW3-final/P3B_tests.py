#!/usr/bin/env python3

import bank.Bank as bank


# Test if trying to withdraw more than balance
def test_over_withdrawal():
    user = bank.BankUser("Joe")
    user.addAccount(bank.AccountType.SAVINGS)
    user.deposit(bank.AccountType.SAVINGS, 10)
    try:
        user.withdraw(bank.AccountType.SAVINGS, 1000)
    except Exception as e:
        print('Error:', e)


# Test if withdrawing and depositing a negative amount
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


# Test if duplicate attempts to create a savings and checking account
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
    # Should still able to access already existing accounts (with no error) --
    user.deposit(bank.AccountType.SAVINGS, 10)
    user.deposit(bank.AccountType.CHECKING, 10)


# Test if account doesn't exist for balance requests, withdrawing, and depositing
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


# TODO: I think need to include further tests to show per hw (maybe use functions, etc.)\
# TODO: but I think just for the BankUser class (could call BankAccount methods from user)

print()

# -- BankAccount() --

# Check that __str__ works
a = bank.BankAccount("Joe", bank.AccountType.CHECKING)
print(a)

# Check that __len__ works
print(len(a))  # Should be 0

# Check deposit() and withdraw()
a.withdraw(0)  # Should not produce an error
a.deposit(10)
print(len(a))
a.withdraw(5)
print(len(a))  # Should be 5

print()

# -- BankUser() --

# Check that __str__ works
user = bank.BankUser("Joe")
print(user)  # Should show no accounts
user.addAccount(bank.AccountType.SAVINGS)
user.addAccount(bank.AccountType.CHECKING)
print(user)  # Should show some accounts

# Check getBalance(), deposit(), and withdraw()
print(user.getBalance(bank.AccountType.SAVINGS))   # Should show 0
print(user.getBalance(bank.AccountType.CHECKING))  # Should show 0
user.deposit(bank.AccountType.SAVINGS, 10)
user.deposit(bank.AccountType.CHECKING, 10)
print(user.getBalance(bank.AccountType.SAVINGS))   # Should show 10
print(user.getBalance(bank.AccountType.CHECKING))  # Should show 10
user.withdraw(bank.AccountType.SAVINGS, 4)
user.withdraw(bank.AccountType.CHECKING, 4)
print(user.getBalance(bank.AccountType.SAVINGS))   # Should show 6
print(user.getBalance(bank.AccountType.CHECKING))  # Should show 6
