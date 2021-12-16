# BankAccount.py
# Author: 
# Date: 

#import Transaction class
from Transaction import *

def main():
    """Display main menu and class functions based on the selected action"""

    print ('Welcome to Bank Account Application')
    print ()

    done = False

    # Create an empty list of transactions
    list_of_transactions = []

    #Loop as long as done is False
    while (not done):
        #Display menu
        print ('===================================')
        print ('A - Read data from the file')
        print ('B - Display list of transactions')
        print ('C - Add a new transaction')
        print ('D - Calculate current balance')
        print ('E - Save data to a file')
        print ('Q - Quit')
        print ('===================================')
        print ('Please select an action by typing A, B, C, D, E, or Q')
        action = input ('? ')

        if (action == 'A' or action == 'a'):
            read_data (list_of_transactions)
        elif (action == 'B' or action == 'b'):
            display_list (list_of_transactions)
        elif (action == 'C' or action == 'c'):
            add_transaction (list_of_transactions)
        elif (action == 'D' or action == 'd'):
            calculate_balance (list_of_transactions)
        elif (action == 'E' or action == 'e'):
            save_data (list_of_transactions)
        elif (action == 'Q' or action == 'q'):
            done = True
        else:
            print ('Incorrect action type. Please try again')

        print ()

    print ('Thank you for using Bank Account Application')

def read_data (list_of_transactions):
    """Read data from the input file, create transaction object and add it to
       the list of transactions"""

       # Ask user for name of the input file, read each line of the data,
       # split line using colon (:) is delimiter, create transaction object
       # and add it to the list of transaction. Display error message if the
       # input file is not found.
    try:
       inputFileName = input('What is the name of the file? ')
       inputFile = open(inputFileName, "r")
       for line in inputFile:
           date = line.split(":")[0]
           transaction_type = line.split(":")[1].lower()
           amount = float(line.split(":")[2])
           transaction = Transaction(date, transaction_type, amount)
           list_of_transactions.append(transaction)
       
    except FileNotFoundError as err:
        #If the file is not found then display an error message
        print("File not found. Please try again.")
      

def display_list (list_of_transactions):
   """ Displays list of transactions """

   # Sort the list of transactions by date and display list of transactions
   # in form of a table

   list_of_transactions.sort(key=Transaction.get_date)
   print('Date       Type        Amount')
   print ('===================================')
   for t in list_of_transactions:
       print(t.date, '     ', t.transaction_type, '         $', "%.2f" % t.amount)

   print ('===================================')
           


def add_transaction (list_of_transactions):
    """Adds a new transaction to list of Transactions"""

    # Ask user for date, type, and amount of transaction, create a transaction
    # object and append it to the list of transactions.
    # Display an error message if the transaction type is not valid or amount
    # is negative. Valid transaction types are deposit, withdraw, bank charge
    # and interest

    date = input('Enter date using the format yyyymmdd: ')
    transaction_type = input('Enter transaction type: ')
    amount = float(input('Enter transaction amount: '))
    if transaction_type == 'deposit' or transaction_type == 'interest' or transaction_type == 'withdraw' or transaction_type == 'bank charge' and amount > 0:
        transaction = Transaction(date, transaction_type, amount)
        list_of_transactions.append(transaction)
    else:
        print('That is not a valid transaction type or amount is less than 0. Please enter "deposit," "interest," "withdraw," or "bank charge," and choose an amount greater than 0.')
    print ('Add Transaction Function')



def calculate_balance (list_of_transactions):

    """Calculates the current balance"""

    # Start with initializing balance to zero
    # For each transaction in the list of transactions you will
    # add the amount to balance if the transaction type is deposit or interest
    # subtract the amount if transaction type is withdraw or bank charge
    # Print the balance on the screen

    balance = 0
    for t in list_of_transactions:
        if t.transaction_type == 'deposit' or t.transaction_type == 'interest':
            balance += t.amount
            print(balance)
        elif t.transaction_type == 'withdraw' or t.transaction_type == 'bank charge':
            balance = balance - t.amount
            print(balance)
        else:
            print('That is not a valid transaction type. Please enter "deposit," "interest," "withdraw," or "bank charge."')
            
        

def save_data (list_of_transactions):
    """ Saves list of transaction to a file"""

    # Ask user for name of the output file, sort the list of transactions by date
    # and save the data using the following format:
    # date:transaction_type:amount
    # Display a message that data was saved to the output file.
    outputFileName = input('What is the name of the output file?' )
    list_of_transactions.sort(key=Transaction.get_date)
    f = open(outputFileName, "w")
    for t in list_of_transactions:
       f.write(t.date + ':' + t.transaction_type + ':' + '%.2f' % t.amount + '\n')
    f.close()
    print("Data was saved.")
            
