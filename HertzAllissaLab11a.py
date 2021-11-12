###########################################################################
# Name: Allissa Hertz
# Date: 11/4/21
# This program will perform the following tasks:
#   1. It will ask the user for a number less than 2 (1, 0, or any
#   negative number. Then, it will display an error message.
#   In the same way it will display an error message if the user enters a non-
#   numerical or a floating point number.
#   2. It will calculate and display all prime numbers between 2
#   and the user entered number.
###########################################################################

###########################################################################
# Function Name: is_prime
# Description: Return ture if the given number is prime,
#              otherwise return false. A number (n) is prime if no
#              number between 2 and the square root of n can evenly divide n.
# Parameter: num - an integer number
# Returns true if the number is prime, otherwise returns false.
###########################################################################

import math
def is_prime(num):
    # Calculate square root of num and convert it into int
    square_root = int(math.sqrt(num))

    #Look at all numbers between 2 and the square root of num
    for n in range(2, square_root+1):
        # if num can be evenly divided by n then num is not prime
        # we can use % operator. If mod is 0 then division was even
        # and num is not prime.
        if(num % n ==0):
            return False

        #if all divisions are not even then the num is prime
    return True

###########################################################################
# Function Name: main
# Description: 
# Ask the user for a number greater than 2. It will use a loop to iterate
# from 2 to the given number and display all the numbers which are prime. It will
# use is_prime function to check if the number is prime.
# It will also display an error message if the input is
# invalid (see program description)
# Parameter: none
#
###########################################################################

def main():

    # Set up loop control variable
    error = True

    # Iterate as long as error is True
    # Writing 'while error' is the same as 'while error = True'
    while error:
        try:
            user_input = int(input('Enter a whole number >= 2: '))
            if user_input < 2:
                print('Input must be >= 2. Please try again.')

            else:
                # If input > 2 then reset error to False to exit the loop
                error = False
                
        except ValueError as err:
            #If input is non numerical then display an error message
            print('Input is non-numerical. Please try again')

    print('The following numbers between 2 and', user_input, 'are prime: ')
    # Use a for loop to iterate through all numbers between 2 and the user input
    for num in range(2, user_input+1):
        # Use is_prime to check if the num is prime
        result = is_prime(num)
        # If result is true, then display the number as prime
        if result:
            print(num, end= ' ')
