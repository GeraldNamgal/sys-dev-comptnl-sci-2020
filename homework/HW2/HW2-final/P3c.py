#!/usr/bin/env python3
# Gerald Arocena
# CSCI E-207, Fall 2020
# HW2, Problem 3c


def make_withdrawal(balance):
    def closure(withdraw_amt):
        nonlocal balance
        print("Initial balance is", balance)
        print("Withdrawing ", withdraw_amt, "...", sep='')
        try:
            if balance - withdraw_amt < 0:
                raise ValueError('insufficient funds for withdrawal amount')
            if withdraw_amt <= 0:
                raise ValueError('please enter an amount more than zero')
        except ValueError as err:
            print("ERROR:", err)
        else:
            print("SUCCESS!")
            balance = balance - withdraw_amt
        print("New balance is", balance)
    return closure


init_balance = 10
withdrawal_amount = 11
new_withdrawal_amount = 10

# Demo...
wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)
