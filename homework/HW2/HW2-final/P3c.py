#!/usr/bin/env python3
def make_withdrawal(balance):
    def closure(withdraw_amt):
        nonlocal balance
        print("Initial balance is", balance)
        print("Withdrawing ", withdraw_amt, "...", sep='')
        try:
            if balance - withdraw_amt < 0:
                raise ValueError('insufficient funds for withdrawal amount')
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
wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)
