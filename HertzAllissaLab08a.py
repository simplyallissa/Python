# Allissa
# Hertz
# Date: 10/20/21
# Description: This program shows techniques of defining function,
# parameter passing and function invocation.

# fahrenToCel function
# parameter: A temperature value in Fahrenheit
# returns equivalent tempature in Celsius

def fahrenToCel(fahren):
    result = (fahren - 32)*(5.0/9.0)
    return result

# fahrenToCellList function
# parameter: a list of temperature values in Fahrenheit
# converts the list to equivalent tempuratures in Celsius
# If you pass a list as an argument, this will change the value in the calling function

def fahrenToCelList(fahrenList):
    for i in range(len(fahrenList)):
        fahren = fahrenList[i]
        celsius = (fahren - 32) * (5.0/9.0)
        fahrenList[i] = round(celsius,2)

# main function

def main():
    fval = float(input("Please enter the temperature in Fahrenheit: "))
    # call the function fahrenToCel
    cval = fahrenToCel(fval)
    print("Equivalent temperature in Celcius is {0:0.2f} ".format(cval))

    fahrenheitList = []
    # Take 5 temperatures as inputs and store them in fahrenhitList
    for i in range(5):
        fahren = float(input("Enter temperature in Fahrenheit: "))
        fahrenheitList.append(fahren)

    # call the function fahrenToCelList
    fahrenToCelList(fahrenheitList)
    print("The converted temperature list")
    print(fahrenheitList)
    
