
import math

def main():

### A. Write a program to determine the length of a ladder required to reach
### a given height when leaned against a hose.

### Input: height, angle
### Output: lenght of ladder required to reach a given height
### when leaned against a house
### Formula: Lenght = height/sin angle

    
    height = int(input("What is the height of the ladder in meters?: "))
    angle = int(input("What is the angle of the ladder in degrees?: "))

    angle_in_radians = angle * (math.pi)/180

    length = int(height/math.sin(angle_in_radians))


    print("Give height= " + str(height) + ", angle= " + str(angle) + "the length is equal to "+ str(length) + " meters.")

### B. Using range and for loop, write a program to find the sume of the first n natural numbers, where the
### value of n is provided by the user

### Input: number provided by user
### Output: sum of the sequential numbers up to the number provided by the user
    
    n = int(input("Please provide a number: "))
    sum = 0
    
    for i in range(1, n+1):
        sum = sum + i

    
    print("The sum of the numbers up to", n, "is", sum)

### C. Implement the following formula for n value that is supplied by a
### user. Discuss, for a given n, how the results compare to part B.

### Input: Start at value k=1, go to value n
### Output: sum of numbers k + 1 up to value n, which will be equal to n(n+1)/2
### Formula: n(n+1)/2

    n = int(input("Please provide a number: "))
    sum = 0
    
    for i in range(1, n+1):
        sum = sum + i

    
    print("The sum of the numbers up to", n, "is", sum)

    m = (n*(n+1))/2

    print("equation return value is: ",m)

### D. Write a program that finds the average of a series of numbers entered by the
### user. As in the previous problem, the program will first ask the user
### how many numbers there are. Note: the average should always be a float,
### even if the user inputs are all ints

### Input: a number of numbers and then a list of numbers entered by the user
### Output: an average in a float
### Formula: sum of a list of numbers divided by number of numbers in the list

    number_of_numbers = int(input("Enter a number of numbers: "))
    number = 0.0
    for i in range(number_of_numbers):
        number += float(input("Enter a number: "))
    average = number/number_of_numbers
    print(average)
    

### E Write a program to find the factorial of number n supplied by a user.

### Input: a number provided by the user
### Output: an average in a float
### Formula: sum of a list of numbers divided by number of numbers in the list

    number_provided = int(input("Enter a number: "))
    factorial = math.factorial(number_provided)
    print(factorial)
        
        
main()
