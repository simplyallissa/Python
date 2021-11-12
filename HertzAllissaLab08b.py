# Allissa
# Hertz
# Date: 10/20/21
# Description: This program converts a date format from
# “mm/dd/yyyy” to “month day, year”


# The datetime module supplies classes for manipulating dates and times
from datetime import datetime


# dateConvert function
# parameter: A date value formatted "mm/dd/yyy"
# returns mm/dd/yy as month day, year
def dateConvert(userDate):
    # strptime takes a date string and changes it into a
    # datetime object where %m represents month, %d
    # represents in two digets and %Y represents year
    # as yyyy
    formattedDate = datetime.strptime(userDate, "%m/%d/%Y")

    # converts datetime object to a different date time object
    # using the datetime module. %B represents full month name,
    # %d represends day of the year as an integer with no
    # leading zeros. %Y represents year as yyyy
    #returns the value to the function.
    return(formattedDate.strftime("%B %-d, %Y"))

# user enters a date
userDate = input("Enter a date in 'mm/yy/yyy' format: ")

# calls the dateConvert function and passes in the date entered by the user
print(dateConvert(userDate))

