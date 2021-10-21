def main():
    word_to_cipher = input("Input a word: ")

    # create an empty list for the even and odd index letters
    ciphered_word_evens = []
    ciphered_word_odds = []

    # loop through the letters in the word
    for letters in range(len(word_to_cipher)):
        # if divisible by 2 (even) add to even array
        if letters % 2 == 0:
            ciphered_word_evens.append(word_to_cipher[letters])
        # otherwise add to odd array
        else:
            ciphered_word_odds.append(word_to_cipher[letters])

    # join together the even array with the odd array to put the odd letters at the end
    cipher = "".join(ciphered_word_evens + ciphered_word_odds)

    print(cipher)

    # empty array to contain the letters after we loop through both arrays and add
    # them one at a time
    deciphered_word = []

    # check which array is longer so there won't be an out of index error with the loop
    # if the even array is longer then the last letter needs to be added to the end
    if len(ciphered_word_odds) < len(ciphered_word_evens):
        x = ciphered_word_odds
        y = ciphered_word_evens[-1]
        # if the odd array is longer then the last letter doesn't need to be added so I just
        # set it to an empty string so there is not an error
    else:
        x = ciphered_word_evens
        y = ""
        
    #here's that loop that adds each letter to the empty array alternating
    for letters in range(len(x)):
        deciphered_word.append(ciphered_word_evens[letters])
        deciphered_word.append(ciphered_word_odds[letters])
    #join the letters in the array and add the extra letter if the even one was longer
    print("".join(deciphered_word) + y)

    
main()
    
    
