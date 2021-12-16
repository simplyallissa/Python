def main():
    year = int(input("Enter a year between 1900-2099: "))
    
    a = year%19
    b = year%4
    c = year%7
    d = ((19 * a) + 24)%3
    e = ((2 * b) + (4 * c) + (6 * d) + 5)%7

    
    date_of_easter = (22 + d + e)

    print("a="+str(a)+"\r\nb="+str(b)+"\r\nc="+str(c)+"\r\nd="+str(d)+"\r\ne="+str(e)
    print(date_of_easter)
    
    if year == 1954 or year == 1981 or year == 2049 or year == 2076:
        date_of_easter -= 7
        print("The date of Easter is April " + str(date_of_easter))
        

    if year > 1900 and year < 2099:
        date_of_easter = 22 + d + e

        if date_of_easter <= 31:
            print("The date of Easter is March " + str(date_of_easter))

        else:
            april_date = date_of_easter - 31
            print("The date of Easter is April " + str(april_date))

main()

