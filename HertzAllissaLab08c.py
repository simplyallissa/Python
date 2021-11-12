# Allissa
# Hertz
# Date: 10/20/21
# Description: Double the values of a list

# findDoubles function
# parameter: list of values
# returns the list of values doubled
def findDoubles(numberList):
    # loop for the number of times that there is items in the list
    for i in range(len(numberList)):
        # assign num as the value at the current list index
        num = numberList[i]
        # double the value 
        double = num + num
        #replace the value at the current list index with the doubled value
        numberList[i] = double

# main function
def main():

    # create a list to add the numbers to
    usersNumbers = []
    # loop 5 times for the five numbers
    for i in range(5):
        # Ask user for a number
        number = int(input("Please enter a number: "))
        # add it to the list of user's numbers 
        usersNumbers.append(number)
    # call the findDoubles and pass in the list of the user's numbers
    findDoubles(usersNumbers)
    # print the doubled lis
    print(usersNumbers)

main()
    
