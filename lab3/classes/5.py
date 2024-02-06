'''Create a bank account class that has attributes owner, balance and two methods deposit and withdraw.
Withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    pass'''
import math
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,d):
        self.balance+=d
        print(f"vash balance popolnen.new balance:({self.balance})")
    def withdraw(self,d):
        if self.balance<d:
            print("v vashem schetu net deneg")
        else:
            self.balance-=d
            print(f"new balance:({self.balance})")
account1 = Account("mua", 1000.0)
account1.deposit(500.0)
account1.withdraw(200.0)
account1.withdraw(1500.0)