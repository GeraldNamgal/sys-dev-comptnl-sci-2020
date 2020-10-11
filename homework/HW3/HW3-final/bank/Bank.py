#!/usr/bin/env python3

from enum import Enum


class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


# TODO: Enum warm-up (delete later)
# print(AccountType.SAVINGS)  # <-- Python representation for an enum
# print(AccountType.SAVINGS == AccountType.SAVINGS)
# print(AccountType.SAVINGS == AccountType.CHECKING)
# print(AccountType.SAVINGS.name)


class BankAccount:
    def __init__(self, owner, accountType: AccountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        try:
            if self.balance - amount < 0:
                raise ValueError('Balance is less than withdrawal amount entered')
            if amount < 0:
                raise ValueError('Withdrawal requires a non-negative amount')
        except Exception:
            raise
        else:
            self.balance -= amount

    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError('Deposit requires a non-negative amount')
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

    def addAccount(self, accountType):
        limitedAcctTypes = [AccountType.SAVINGS, AccountType.CHECKING]
        try:
            if accountType in limitedAcctTypes:
                for account_key in self.accounts:
                    if account_key == accountType:
                        raise ValueError(f'Can only have one {accountType.name}'
                                         f' account')
        except Exception:
            raise
        else:
            self.accounts[accountType] = BankAccount(self.owner, accountType)

    def getBalance(self, accountType):
        try:
            if accountType not in self.accounts:
                raise ValueError(f'That account does not exist; cannot get balance')
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
                raise ValueError(f'That account does not exist; cannot withdraw')
        except Exception:
            raise
        else:
            self.accounts[accountType].withdraw(amount)

    def __str__(self):
        info = 'User has the following accounts:'
        for account in self.accounts:
            info += '\n{0}'.format(account.name)
        return info


# TODO: Test BankUser's str function and overall functioning as defined in hw (interface, etc.)
