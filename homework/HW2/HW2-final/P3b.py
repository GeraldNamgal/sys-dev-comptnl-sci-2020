#!/usr/bin/env python3
# Gerald Arocena
# CSCI E-207, Fall 2020
# HW2, Problem 3b


print("This program causes an error because the 'balance' name gets "
      + "redefined in the 'else' block of code (in the inner function) when "
      + "the outer function is called and thus becomes bound to a different "
      + "object altogether from that of the parameter 'balance' that was "
      + "passed in to the outer function. This also changes the lexical scope "
      + "of 'balance' to within the scope of the inner function (i.e., it "
      + "becomes a local variable of the inner function block since it was "
      + "redefined there). Essentially, the reference to the parameter "
      + "'balance' that was passed in to the outer function gets lost. And "
      + "because the use of a name in Python is resolved using the nearest "
      + "enclosing scope, an 'UnboundLocalError' is thrown when the inner "
      + "'closure' function is called because it attempts to use 'balance' "
      + "before it has been defined.\n")


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
