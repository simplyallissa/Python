import string

def main():

    uppercase_ascii = string.ascii_uppercase
    individual_ascii_characters = list(uppercase_ascii)
    number_of_ascii_characters = len(uppercase_ascii)

    for x in range(number_of_ascii_characters):
        print(ord(individual_ascii_characters[x]))

main()
