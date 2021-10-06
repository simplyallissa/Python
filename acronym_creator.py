def main():
    ###I got this list of prepositions out of a stop words library
    prepositions = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    user_input = input("Enter a phrase to create an acronym for: ")
    ###You have to declare letters as an empty string so that it considers the letter that is in the first word before the loop starts
    letters = ""
    ###You have to split the string put in by the user into individual words so each one
    ###can be sequenced
    words = user_input.split()
    ### for a word in the user input
    for word in words:
        ###if a word is in the array of prepositions
        if word in prepositions:
        ###skip word
            pass
        else:
            #the first letter defited by index 0 of the word
            letters = letters + word[0]
    #join together the letters with no space as uppercase letters
    print("".join(letters).upper())

main()
