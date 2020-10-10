#!/usr/bin/env python3

from enum import Enum  # TODO: Enum warm-up (delete later)


class AccountType(Enum):  # TODO: Enum warm-up (delete later)
    SAVINGS = 1
    CHECKING = 2


# TODO: Enum warm-up (delete later)
print(AccountType.SAVINGS)  # <-- Python representation for an enum
print(AccountType.SAVINGS == AccountType.SAVINGS)
print(AccountType.SAVINGS == AccountType.CHECKING)
print(AccountType.SAVINGS.name)


class BankAccount:
    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0

    def withdraw(self, amount):
        try:
            if self.balance - amount < 0:
                raise ValueError('insufficient funds for withdrawal amount')
            if amount < 0:
                raise ValueError('please enter a non-negative amount')
        except ValueError as err:
            print("ERROR:", err)
        # TODO -- else:

    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError('please enter a non-negative amount')
        except ValueError as err:
            print("ERROR:", err)
        # TODO -- else:

    def __str__(self):
        return 'This account belongs to {0}'.format(self.owner)

    def __len__(self):
        return self.balance
