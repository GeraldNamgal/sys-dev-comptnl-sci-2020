#!/usr/bin/env python3
print("This program does not behave correctly ('under the hood') because "
      + "it's not updating the value of the 'balance' object stored in memory "
      + "that was passed in to the outer function 'make_withdrawal()'. The "
      + "value of the object 'balance' refers to in this case is set on the "
      + "call to 'make_withdrawal()' when it is captured by the inner function "
      + "after which it can not be changed via calls to the returned inner "
      + "'closure' function. An error would occur if 'balance' was reassigned "
      + "in the inner function. This process is called encapsulation which is "
      + "useful for protecting against modifying state incorrectly.\n")


def make_withdrawal(balance):
    def closure(withdraw_amt):
        print("Initial balance is", balance)
        print("Withdrawing ", withdraw_amt, "...", sep='')
        try:
            if balance - withdraw_amt < 0:
                raise ValueError('insufficient funds for withdrawal amount')
            if withdraw_amt <= 0:
                raise ValueError('please enter an amount more than zero')
        except ValueError as err:
            print("ERROR:", err)
            print("New balance is", balance)
        else:
            print("SUCCESS!")
            print("New balance is", balance - withdraw_amt)
    return closure


init_balance = 10
withdrawal_amount = 11
new_withdrawal_amount = 10

# Demo...
wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)
