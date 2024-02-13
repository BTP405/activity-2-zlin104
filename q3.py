def wordCount(t):
    wordBook = {}
    f = open(t, "r")

    # enumerate(f, l) returns the index of line and the line in the file 
    for record, line in enumerate(f, 1):
        # split string into a list 
        words = line.split()
        
        for word in words:
            # make the word lowercase and remove a set of symbols in the word
            word = word.lower().strip(",.?!-:;")
            if word not in wordBook:
                """
                create a new entry with the word as the key
                and initialize its value as a list containing the current line number

                """
                wordBook[word] = [record]
                
            elif record not in wordBook[word]:
                #add the new line number into the key's value
                wordBook[word].append(record)
                
    return wordBook


"""
test line
print(wordCount('t.txt'))
"""
