def main():
    age = int(input('What is your age? '))
    years_of_citizenship = int(input('How many years have you been a citizen? '))
    senator_eligible = False
    representative_eligible = False
    
    
    if age > 29 and years_of_citizenship > 8:
        senator_eligible = True
        
    if age > 25 and years_of_citizenship > 7:
        representative_eligible = True

    if senator_eligible == True and representative_eligible == True:
        print("You are eligible to be a senator or a represenative")
    elif senator_eligible == True:
        print("You are eligible to be a senator")
    elif representative_eligible == True:
        print("You are eligible to be a representative")
    else:
        print("You are not eligible to be a senator or a representative")
        
        
    
