###########################################################################
# Name: Allissa Hertz
# Date: 10/28/21
# Description: This program will perform the following tasks:
#       1) It will ask the user for a number of packages purchased
#       2) It will calculate the discount precentage, discount amount, and total amount
#       3) It will display an error message if the entered amount is less than 0
###########################################################################

###########################################################################
# Function name: discount_percentage
# Description: Calculate discount precentage based on number of packages bought
# Parametere: number of packages
# Returns a discount percentage
###########################################################################

def discount_percentage(number_of_packages):
    number_of_packages = int(number_of_packages)
    if number_of_packages >= 100:
        discount = '50'
    elif number_of_packages >= 50:
        discount = '40'
    elif number_of_packages >= 20:
        discount = '30'
    elif number_of_packages >= 10:
        discount = '20'
    else:
        discount = '0'

    return discount

###########################################################################
# Function name: main
# Description: Ask the user for a number of packages purchased. Calculate the
# total price of all packages, the discount amount, and the cost after the
# discount. Display all three.
# It uses try/except construct to catch any errors and displays
# appropriate error messages
# Parameter: None
# Returns: None
###########################################################################

def main():

    try:
        number_of_packages = int(input('How many packages did you purchase?: '))
        if number_of_packages < 1:
            print("Number of packages cannot be 0 or less.")
            return
        
        amount_of_discount = int(discount_percentage(number_of_packages))
        price = (float(number_of_packages) * 99)
        discount_amount = price * (amount_of_discount/100)
        discounted_price = price - discount_amount
        print("You recieved a discount amount of: {0}%\n".format(amount_of_discount) + "Your discount amount is ${0:.2f}\n".format(discount_amount) +"Your price after discount is ${0:.2f}".format(discounted_price))

            # Catch unexpected errors
    except:
        print('Unknown error')
