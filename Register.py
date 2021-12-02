# register.py
# Name: Allissa Hertz
# Date: 11/30/21

from BankAccount import *

def main():
    
    # Create a BankAccount object from the BankAccount class
    BA = BankAccount()

    #Ask for a number of transactions to perform
    amount_of_transactions = int(input('Enter a number of transactions: '))
    #count for successful transactions
    count = 0

    for i in range(amount_of_transactions):
        #Ask for a transaction type and amount for each transaction
        transaction_type = input('Enter a type of transaction: ').lower()
        transaction_amount = float(input('Enter a transaction amount: '))
        #If it's a deposit, use the deposit class with the amount entered to eval whether to
        #make the deposit or print the error if it's less than 0.
        if transaction_type == "deposit":
            if BA.deposit(transaction_amount) == False:
                print('Deposit amount ${0:.2f} is less than 0. Transaction rejected.'.format(transaction_amount))
            else:
                #count for successful transactions + 1
                count += 1
                print('Transaction was successful. Your account balance is ${0:.2f}.'.format(BA.getBalance()))
        #If it's a withdraw, use the withdraw class with the amount entered to eval whether to
        #make the withdraw or print the error if it's higher than the balance                
        elif transaction_type == "withdraw":
            if BA.withdraw(transaction_amount) == False:
                print('Withdraw amount ${0:.2f} is higher than balance of ${1:.2f}.Transaction rejected.'.format(transaction_amount, BA.getBalance()))
            else:
                #count for successful transactions + 1
                count += 1
                print('Transaction was successful. Your account balance is ${0:.2f}.'.format(BA.getBalance()))
        else:
            # If they don't type "withdraw" or "deposit" then print an error
            print('That is not a valid transaction type. Please enter withdraw or deposit.')
    #Display number of transactions and balance after all transactions
    print('After {0:.0f} transactions, your balance is: ${1:.2f}'.format(count, BA.getBalance()))
