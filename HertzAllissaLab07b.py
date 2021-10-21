# Allissa
# Hertz
# Oct 11, 2021
# Description: This program shows techniques of reading and writing text files in Python.

import math

def main():

    # Ask for the name of the input file
    inputFileName = input("Enter the input file name: ")

    # Open the input file
    inputFile = open(inputFileName, "r")

    # Ask what the output file name should be
    outputFileName = input("Enter the output file name: ")

    # Open the output file
    outputFile = open(outputFileName, "w")

    # Process each line of the input file
    for line in inputFile:
        # Set the score back to zero each time the inner loop is completed
        # so that the scores are added per line
        score = 0
        # Get the name of each person from index 0
        name = line.split()[0]
        # Loop through each value split by whitespace. The name is skipped by
        # starting at 1 instead of zero
        for i in range(1, len(line.split()), 1):
            # Each split value is added together and set to be "score"
            score += int(line.split()[i])
            # Find the average by dividing the score by the number of items
            # minus the one, which was the name. Set it to a str
            # so it can be split by index
            average = str(score/int(len(line.split()) -1))
            # Find the index of the string at the decimal point
            d = average.index(".")
            # write to the output file the name and then the average score truncated at the index
            # value of the decimal point + 2 places (So all number come out as
            # unrounded floats
        print(name,average[:d + 2], file=outputFile)

    inputFile.close()
    outputFile.close()

main()
