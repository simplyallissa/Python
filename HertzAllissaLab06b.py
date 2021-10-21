# Allissa
# Hertz
# Oct. 6
# Description: Lab 6. Caeser cipher

def main():

    word_to_cipher = input("Input a word to cipher: ")
    number_for_cipher = input("Input a number: ")

    # create an empty list for the ciphered and deciphered letters
    ciphered_word = []
    deciphered_word = []
    
    # loop through the word the user put in
    for ch in word_to_cipher:
        # find the ord value of each character, add the number the user put in and turn it
        # back into a character
        c = chr(ord(ch) + int(number_for_cipher))
        # find the ord value of each character, subtract the number the user put in and turn it
        # back into a character
        d = chr(ord(c) - int(number_for_cipher))
        # add each ciphered/deciphered character to the empty list
        ciphered_word.append(c)
        deciphered_word.append(d)

    # Print "The encode/decode message is" along with all the letters in the ciphered/deciphered
    # list joined together with no characters/spaces
    print("The encoded message is:", "".join(ciphered_word))
    print("The decoded message is:", "".join(deciphered_word))

main()
