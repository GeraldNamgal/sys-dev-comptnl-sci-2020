#!/usr/bin/env python3
def make_withdrawal(balance):
    def closure(withdraw_amt):
        print("Initial balance is", balance)
        print("Withdrawing ", withdraw_amt, "...", sep='')
        try:
            if balance - withdraw_amt < 0:
                raise ValueError('insufficient funds for withdrawal amount')
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
wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)


print("The above program does not behave correctly because it's not updating "
      + "the value of the 'balance' object stored in memory that was passed in "
      + "to the outter function 'make_withdrawal()'. The value of 'balance' in "
      + "this case is set on the call to 'make_withdrawal' and can not be "
      + "changed from calls to the inner closure function.")
