###########################################################################
# Name: Allissa Hertz
# Date: 11/4/21
# This program will perform the following tasks:
#   1. It will ask the user for a word and the name of a file.
#   2. It will calculate and display the number of times a word
#   appears in the file
###########################################################################

import os
    

def main():

    number_of_words = 0

    try:
        user_input_file_name = input("Enter the name of a file: ")
        user_input_word = input("Enter a word that you would like to find in the file: ")
        file = open(user_input_file_name, "r")
            
        # Read each line in the file
        for line in file:
            # Read each word in the line
            for word in line.split():
                # If the word is the same as the word the user input
                if word == user_input_word:
                    # add one to the number_of_words value
                    number_of_words += 1

        print("Your word appeared", number_of_words, "times.")
        file.close()
                

    except FileNotFoundError as err:
        #If the file is not found then display an error message
        print(f"File '{user_input_file_name}' not found. Please try again.")
        
main()
