# BankAccount.py
# Name: Allissa Hertz
# Date: 11/30/21

class BankAccount:
    """BankAccount class, which manages withdraws, deposits,
       and keeps track of the account balance"""

    def __init__(self):
        """Set the balance to zero"""
        self.balance = 0

    def deposit(self, amount):
        """If the amount deposited is greater than 0, don't allow the deposit"""
        if amount < 0:
            return False
        else:
            self.balance = self.balance + amount
            return True

    def withdraw(self, amount):
        """If the amount is greater than the balance, don't allow the withdraw"""
        if amount > self.balance:
            return False
        else:
            self.balance = self.balance - amount
            return True

    def getBalance(self):
        """Return the balance"""
        return self.balance
        
        
