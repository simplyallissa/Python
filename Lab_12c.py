def main():

    count = 0
    sum = 0
    infile = open ('data12.txt', 'r')

    line = infile.readline()
    while line != "":
        
        my_list = line.split(',')
        for num in my_list:
            sum = sum + float (num)
            count = count + 1            

    
    infile.close()

    average = sum / count

    print ('Number of data:', count)
    print ('Sum of numbers is:', sum)
    print ('Average is: {0:.2f}'.format(average))
    
