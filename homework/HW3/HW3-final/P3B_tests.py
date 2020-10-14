#!/usr/bin/env python3

import bank.Bank as bank


# Test if trying to withdraw more than balance
def test_over_withdrawal():
    user = bank.BankUser('Joe')
    user.addAccount(bank.AccountType.SAVINGS)
    user.deposit(bank.AccountType.SAVINGS, 10)
    try:
        user.withdraw(bank.AccountType.SAVINGS, 1000)
    except Exception as e:
        print(e)


# Test if withdrawing and depositing a negative amount
def test_negative_amount():
    user = bank.BankUser('Joe')
    user.addAccount(bank.AccountType.SAVINGS)
    try:
        user.withdraw(bank.AccountType.SAVINGS, -10)
    except Exception as e:
        print(e)
    try:
        user.deposit(bank.AccountType.SAVINGS, -10)
    except Exception as e:
        print(e)


# Test if duplicate attempts to create a savings and checking account
def test_duplicate_accounts():
    user = bank.BankUser('Joe')
    user.addAccount(bank.AccountType.SAVINGS)
    user.addAccount(bank.AccountType.CHECKING)
    try:
        user.addAccount(bank.AccountType.SAVINGS)
    except Exception as e:
        print(e)
    try:
        user.addAccount(bank.AccountType.CHECKING)
    except Exception as e:
        print(e)
    # Should still able to access already existing accounts (with no error) --
    user.deposit(bank.AccountType.SAVINGS, 10)
    user.deposit(bank.AccountType.CHECKING, 10)


# Test if account doesn't exist for getBalance, withdraw, and deposit
def test_account_exists():
    user = bank.BankUser('Joe')
    try:
        user.getBalance(bank.AccountType.SAVINGS)
    except Exception as e:
        print(e)
    try:
        user.deposit(bank.AccountType.CHECKING, 10)
    except Exception as e:
        print(e)
    try:
        user.withdraw(bank.AccountType.CHECKING, 10)
    except Exception as e:
        print(e)


# Call exception error test functions above
print('EXCEPTION ERROR TESTS -- \n')
print('- Calling test_over_withdrawal() returns...')
test_over_withdrawal()
print('\n- Calling test_negative_amount() returns...')
test_negative_amount()
print('\n- Calling test_duplicate_accounts() returns...')
test_duplicate_accounts()
print('\n- Calling test_account_exists() returns...')
test_account_exists()

# Additional tests
print('\nADDITIONAL TESTS -- \n')
# BankAccount class
print('BankAccount class:\n')
account = bank.BankAccount('Joe', bank.AccountType.CHECKING)
print(f'- Created \'account\' via calling BankAccount(\'Joe\', '
      f'bank.AccountType.CHECKING)')
print(f'\n- Calling print(account) returns...')
print(account)              # Check that __str__ works
# BankUser class
print('\nBankUser class:\n')
user = bank.BankUser('Joe')
print('- Created \'user\' via calling BankUser(\'Joe\')')
print('\n- Calling print(user) returns...')
print(user)                 # Check that __str__ works (should show no accounts)
user.addAccount(bank.AccountType.SAVINGS)
print('\n- Added SAVINGS account')
user.addAccount(bank.AccountType.CHECKING)
print('\n- Added CHECKING account')
print('\n- Calling print(user) returns...')
print(user)                 # Should show SAVINGS and CHECKING accounts
print(f'\n- SAVINGS balance is: '
      f'{user.getBalance(bank.AccountType.SAVINGS)}')   # Should show 0
print(f'\n- CHECKING balance is: '
      f'{user.getBalance(bank.AccountType.CHECKING)}')  # Should show 0
user.deposit(bank.AccountType.SAVINGS, 10)
print(f'\n- Deposited 10 into SAVINGS')
user.deposit(bank.AccountType.CHECKING, 10)
print(f'\n- Deposited 10 into CHECKING')
print(f'\n- SAVINGS balance is: '
      f'{user.getBalance(bank.AccountType.SAVINGS)}')   # Should show 10
print(f'\n- CHECKING balance is: '
      f'{user.getBalance(bank.AccountType.CHECKING)}')  # Should show 10
user.withdraw(bank.AccountType.SAVINGS, 4)
print('\n- Withdrew 4 from SAVINGS')
user.withdraw(bank.AccountType.CHECKING, 4)
print('\n- Withdrew 4 from CHECKING')
print(f'\n- SAVINGS balance is: '
      f'{user.getBalance(bank.AccountType.SAVINGS)}')   # Should show 6
print(f'\n- CHECKING balance is: '
      f'{user.getBalance(bank.AccountType.CHECKING)}')  # Should show 6

# TODO: Fix commenting to make sense, wherever
