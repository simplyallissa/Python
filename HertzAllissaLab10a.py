###########################################################################
# Name: Allissa Hertz
# Date: 10/28/21
# Description: This program will perform the following tasks:
#       1) It will ask the user for 3 test scores.
#       2) It will calculate the mean of the three test scores
#       3) It will convert the mean into a letter grade (See
#          find_letter_grade function for the mapping)
#       4) It will display an error message if the entered score is non-numerical
###########################################################################

###########################################################################
# Function name: calculate_mean
# Description: Calculate mean of three test scores
# Parametere: score1 - Score for test 1
#             score2 - Score for test 2
#             score3 - Score for test 3
# Returns mean of the three test scores
###########################################################################

def calculate_mean(score1, score2, score3):
    mean = (score1 + score2 + score3) /3

    return mean

##############################################################
# Function name: find_letter_grade
# Description: Convert the mean into letter grade as follows:
#           Mean                        Letter Grade
#           90 to 100                       A
#           80 to 89                        B
#           70 to 79                        C
#           60 to 69                        D
#           0 to 59                         F
# If the score is above 100 or below 0, then it will return undefined
# Parameter: mean- mean of the test scores
# Returns letter grade
##############################################################

def find_letter_grade(mean):
    if mean > 100:
        letter_grade = 'Undefined'
    elif mean >= 90:
        letter_grade = 'A'
    elif mean >= 80:
        letter_grade = 'B'
    elif mean >= 70:
        letter_grade = 'C'
    elif mean >= 60:
        letter_grade = 'D'
    elif mean >= 0:
        letter_grade = 'F'
    else:
        letter_grade = 'Undefined'

    return letter_grade


###########################################################################
# Function name: main
# Description: Ask the user for three test scores, use calculate_mean function to
# calculate the mean, use find_letter_grade function to convert mean into letter grade,
# and display mean and letter grade.
# It uses try/except construct to catch any errors and displays
# appropriate error messages
# Parameter: None
# Returns: None
###########################################################################

def main():
    print('This program will calculate the mean of three test scores and')
    print('convert the mean into a letter grade')
    print ('=============================================================')

    # Use try/except block to catch errors
    try:
        score1 = int(input('Enter score 1: '))
        score2 = int(input('Enter score 2: '))
        score3 = int(input('Enter score 3: '))

        mean = calculate_mean(score1, score2, score3)

        letter_grade = find_letter_grade(mean)

        print ('Your mean score is {0:.3f}'.format(mean))

        print('Your letter grade is: ', letter_grade)

    # If the input is a non-numerical string then display an error message
    except ValueError as err:
        print('One of your scores is non-numeric.')
        print('Please try again with the correct scores')

    # Catch unexpected errors
    except:
        print('Unkown error')

        
        
              
