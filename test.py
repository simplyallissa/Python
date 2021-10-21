def main():
    # open the input file
    inputFile = open("temps.txt", "r")
    # initalize an array to store all the max temps in
    temps = []
    # set the current month to the first month from the file
    currentMonth = "01"
    # initialize the max temp variable
    maxTemp = 0
    #process each line of the input file
    for line in inputFile:
        # split the date and tempurature by white space
        date, tempurature = line.split()
        # split the date into a month and a day
        month, day = date.split("/")
        # as we go through the lines in the file check if the month is different. 
        if currentMonth != month:
            # if it is we change current month to the new month from the line
            currentMonth = month
            # we already changed moths, so I'm subtracting 1 and changing it to an int takes off the zero
            lastMonth = int(month) -1
            # converting each number to the typed up month to be fancy
            if lastMonth == 1:
                lastMonth = "Janurary"
            if lastMonth == 2:
                lastMonth = "Feburary"
            if lastMonth == 3:
                lastMonth = "March"
            if lastMonth == 4:
                lastMonth = "April"
            if lastMonth == 5:
                lastMonth = "May"
            if lastMonth == 6:
                lastMonth = "June"
            if lastMonth == 7:
                lastMonth = "July"
            if lastMonth == 8:
                lastMonth = "August"
            if lastMonth == 9:
                lastMonth = "September"
            if lastMonth == 10:
                lastMonth = "October"
            if lastMonth == 11:
                lastMonth = "November"
            if lastMonth == 12:
                lastMonth = "December"
            # if the month is over then store the max temp in the temps array
            temps.append("The hotest day of " + str(lastMonth) + " was the " + str(dayOfMaxTemp) + " with a max temp of " + str(maxTemp) + "°.")
            # set the max temp back to zero so we start the new month comparing new temps
            maxTemp = 0
        # if the month hasn't changed then we go here and compare the tempurature on that line to
        # the tempurature on the line before
        if int(tempurature) > maxTemp:
            #if the value is bigger then it becomes the max temp now
            maxTemp = int(tempurature)
            # adding the suffixes for the day
            dayOfMaxTemp = int(day)
            if dayOfMaxTemp == 1:
                dayOfMaxTemp = "1st"
            elif dayOfMaxTemp == 2:
                dayOfMaxTemp = "2nd"
            elif dayOfMaxTemp == 3:
                dayOfMaxTemp = "3rd"
            else:
                dayOfMaxTemp = str(dayOfMaxTemp) + "th"
    #since the tempurature doesn't change for the last month, that max temp is added here.
    temps.append("The hotest day of December was the " + dayOfMaxTemp + " with a max temp of " + str(maxTemp))
    print("\n".join(temps))
                   
main()
    
    
