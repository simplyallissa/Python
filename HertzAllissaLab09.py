# Allissa
# Hertz
# Date: 10/27/21
# Description: This program shows techniques of modular programming and testing.

import math

##############################################################
# Function Name: main
# Description: Reads the data from an input file, calculatea the sum, mean
# & standard deviation, and writes the result to an output file
# Parameter: none
# Returns sum, mean, and standard deviation
##############################################################

def main():
    # Ask user for input
    inputFile = input("What is the name of the input file?: ")
    outputFile = input("What is the name of the output file?: ")
    # Get values returned from functions
    my_list = read_data(inputFile)
    sum = compute_sum(my_list)
    mean = compute_mean(my_list)
    sd = compute_sd(my_list)
    # Write to output file
    write_result(outputFile, sum, mean, sd)
    

##############################################################
# Function Name: read_data
# Description: Reads a set of numbers from an input file.
# Parameter: file_name - name of the input file
# Returns list of numbers
##############################################################

def read_data(file_name):
    # Open the input file
    inputFile = open(file_name, "r")
    # Initalize an empty list
    list_of_numbers = []

    # Process each line of the input file
    for line in inputFile:
        # Convert the line into an integer
        number = int(line)
        # Add integer to the list
        list_of_numbers.append(number)
    # Close File
    inputFile.close()
    # Return list
    return list_of_numbers

##############################################################
# Function Name: compute_sum
# Description: Computes the sum of numbers in a list
# Parameter: my_list - name of a list of numbers
# Returns the sum of a list of numbers
##############################################################


def compute_sum(my_list):
    # Initalize strating sum
    sum = 0
    # Process each number in the list
    for number in my_list:
        sum = sum+number
    # Return sum
    return sum


##############################################################
# Function Name: compute_mean
# Description: Computes the mean of numbers in a list
# Parameter: my_list - name of a list of numbers
# Returns the mean of a list of numbers
##############################################################
    
        
def compute_mean(my_list):
    # Find length of list
    size_of_list = len(my_list)
    # Find sum of numbers in list
    sum = compute_sum(my_list)
    # Divide sum by size to get mean
    mean = sum/size_of_list
    # Return mean
    return mean


##############################################################
# Function Name: compute_sd
# Description: Computes the standard deviation of numbers in a list
# Parameter: my_list - name of a list of numbers
# Returns the standard deviation of a list of numbers
##############################################################


def compute_sd(my_list):
    # Calculate mean
    mean = compute_mean(my_list)
    # Initalize starting sum
    sum = 0
    # Use definite loop 
    for num in my_list:
        # Calculate deviation by subtracting mean from the num
        deviation = num - mean
        # Calculate the sqare of the deviation
        deviation *= deviation
        # Add the sqare of the deviation to the sum
        sum += deviation
        deviation = 0
    # Calculate the size of the list
    size_of_list = len(my_list)
    # Divide sum by the size-1 to compute the result
    result = sum/(size_of_list - 1)
    # Take the square root of the result to get the standard deviation
    sd = math.sqrt(result)
    # Return the standard deviation
    return sd


##############################################################
# Function Name: write_result
# Description: Computes the standard deviation of numbers in a list
# Parameter: my_list - name of a list of numbers
# Returns the standard deviation of a list of numbers
##############################################################


def write_result(file_name, sum, mean, sd):
    # Open the output file
    outputFile = open(file_name, "w")
    # Round everything to 2 decimal points
    sum = round(sum,2)
    mean = round(mean,2)
    sd = round(sd,2)
    # Write the values to the output file
    outputFile.write("Sum is: " + str(sum) + "\n")
    outputFile.write("Mean is: " + str(mean) + "\n")
    outputFile.write("Standard Deviation is: " +str(sd) + "\n")
    outputFile.close()
    
    



        
