#!/usr/bin/env python3

from enum import Enum


class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    

class BankAccount:
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        try:
            if self.balance - amount < 0:
                raise ValueError('Balance is less than withdrawal amount '
                                 'entered; withdrawal cancelled')
            if amount < 0:
                raise ValueError('Withdrawal requires a non-negative amount; '
                                 'withdrawal cancelled')
        except Exception:
            raise
        else:
            self.balance -= amount

    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError('Deposit requires a non-negative amount; '
                                 'deposit cancelled')
        except Exception:
            raise
        else:
            self.balance += amount

    def __str__(self):
        return 'This {0} account belongs to {1}'.format(self.accountType.name,
                                                        self.owner)

    def __len__(self):
        return self.balance


class BankUser:
    def __init__(self, owner):
        self.owner = owner
        self.accounts = {}
        self.limitedAcctTypes = [AccountType.SAVINGS, AccountType.CHECKING]

    def addAccount(self, accountType):
        try:
            if accountType in self.limitedAcctTypes:   # Only one type allowed?
                for account_key in self.accounts:      # Check if already exists
                    if account_key == accountType:
                        raise ValueError(f'Can only have one {accountType.name}'
                                         f' account; account not created')
        except Exception:
            raise
        else:
            self.accounts[accountType] = BankAccount(self.owner, accountType)

    def getBalance(self, accountType):
        try:
            if accountType not in self.accounts:
                raise ValueError(f'That account does not exist; '
                                 f'cannot get balance')
        except Exception:
            raise
        else:
            return len(self.accounts[accountType])

    def deposit(self, accountType, amount):
        try:
            if accountType not in self.accounts:
                raise ValueError(f'That account does not exist; cannot deposit')
        except Exception:
            raise
        else:
            self.accounts[accountType].deposit(amount)

    def withdraw(self, accountType, amount):
        try:
            if accountType not in self.accounts:
                raise ValueError(f'That account does not exist; '
                                 f'cannot withdraw')
        except Exception:
            raise
        else:
            self.accounts[accountType].withdraw(amount)

    def __str__(self):
        info = 'User has the following accounts:'
        if not self.accounts:
            info += '\nNone'
        else:
            for account in self.accounts:
                info += '\n{0}'.format(account.name)
        return info


def ATMSession(bankUser: BankUser):
    def Interface():
        while True:
            print(f'Enter Option:\n'
                  f'1)Exit\n'
                  f'2)Create Account\n'
                  f'3)Check Balance\n'
                  f'4)Deposit\n'
                  f'5)Withdraw')
            choice1 = input()
            if not choice1.isnumeric():
                print('\nERROR: Invalid Choice. Try Again --\n')
                continue
            choice1 = int(choice1)
            if choice1 == 1:
                break
            elif 2 <= choice1 <= 5:
                print(f'Enter Option:\n'
                      f'1)Checking\n'
                      f'2)Savings')
                choice2 = input()
                if not choice2.isnumeric():
                    print('\nERROR: Invalid Choice. Try Again --\n')
                    continue
                choice2 = int(choice2)
                if 1 <= choice2 <= 2:
                    if choice1 == 2 and choice2 == 1:
                        try:
                            bankUser.addAccount(AccountType.CHECKING)
                            print(f'\nACCOUNT CREATED\n')
                        except Exception as err:
                            print(f'\nERROR: {err}. Try again --\n')
                    elif choice1 == 2 and choice2 == 2:
                        try:
                            bankUser.addAccount(AccountType.SAVINGS)
                            print(f'\nACCOUNT CREATED\n')
                        except Exception as err:
                            print(f'\nERROR: {err}. Try again --\n')
                    elif choice1 == 3 and choice2 == 1:
                        try:
                            balance = bankUser.getBalance(AccountType.CHECKING)
                            print(f'\nBALANCE: {balance}\n')
                        except Exception as err:
                            print(f'\nERROR: {err}. Try again --\n')
                    elif choice1 == 3 and choice2 == 2:
                        try:
                            balance = bankUser.getBalance(AccountType.SAVINGS)
                            print(f'\nBALANCE: {balance}\n')
                        except Exception as err:
                            print(f'\nERROR: {err}. Try again --\n')
                    elif 4 <= choice1 <= 5:
                        print(f'Enter Integer Amount, Cannot Be Negative:')
                        amount = input()
                        if not amount.isnumeric():
                            print('\nERROR: Invalid Amount. Try Again --\n')
                            continue
                        amount = int(amount)
                        if choice1 == 4 and choice2 == 1:
                            try:
                                bankUser.deposit(AccountType.CHECKING, amount)
                                print(f'\nDEPOSITED {amount}\n')
                            except Exception as err:
                                print(f'\nERROR: {err}. Try again --\n')
                        elif choice1 == 4 and choice2 == 2:
                            try:
                                bankUser.deposit(AccountType.SAVINGS, amount)
                                print(f'\nDEPOSITED {amount}\n')
                            except Exception as err:
                                print(f'\nERROR: {err}. Try again --\n')
                        elif choice1 == 5 and choice2 == 1:
                            try:
                                bankUser.withdraw(AccountType.CHECKING, amount)
                                print(f'\nWITHDREW {amount}\n')
                            except Exception as err:
                                print(f'\nERROR: {err}. Try again --\n')
                        elif choice1 == 5 and choice2 == 2:
                            try:
                                bankUser.withdraw(AccountType.SAVINGS, amount)
                                print(f'\nWITHDREW {amount}\n')
                            except Exception as err:
                                print(f'\nERROR: {err}. Try again --\n')
                else:
                    print('\nERROR: Invalid Choice. Try Again --\n')
            else:
                print('\nERROR: Invalid Choice. Try Again --\n')
    return Interface


# TODO: Demoing...
user = BankUser("Joe")
interface = ATMSession(user)
interface()


# References:
# - https://help.semmle.com/wiki/pages/viewpage.action?pageId=29394142
# - https://www.geeksforgeeks.org/python-string-isnumeric-application/
