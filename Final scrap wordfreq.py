def tokenize(lines):  # We define a function that adds an element (word, digit or symbol)
    words = []        # to the list "words"
    for line in lines:
        start = 0
        line = line.strip()
        while start < len(line):  

            while start < len(line) and line[start].isspace():  # If there is a space, start increments
                start = start + 1                                 # so we avoid empty spaces.

            if line[start].isdigit():             # If there is a digit we will add it to the list words
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end + 1
                words.append(line[start:end])
                start = end

            elif line[start].isalpha():          # If we encounter letters we add them together to form the
                end = start                      # the expected word and then we also lowers to not have any captial letters.
                while end < len(line) and line[end].isalpha():
                    end = end + 1
                words.append(line[start:end].lower())
                start = end

            else:                              # If its not a letter, digit or a space, we have a symbol and this will
                                               # also be added to the list.
                words.append(line[start])

                start = start + 1

    return words


def countWords(words, stopwords):   # Defining a function to count the words execpt stopwords in the text/article and
    dict = {}                       # adding them to a dictionary.
    for i in range (0,len(words)):
        if words[i] in stopwords:
            i += 1
        else:
            dict[words[i]] = dict.get(words[i],0) + 1
    return dict

def freq(key_value):         # A small function to help with sorting the items in the dictionary
    return key_value[1]      # to go from higher count to lower.

def printTopMost(dict,n):       # Function that prints out the n most counted words in the dictionary.
    if len(dict)== 0: return ''    
    dictitems = list(dict.items()) 
    dictitems.sort()                           
    dictitems.sort(key=freq, reverse = True)       # Sorts the value from highest to lowest with help from the freq function.
    for i in range(n):                            # loop the n amount of words we want to display
       word, frequency = dictitems[i]             # and displays the word and the frequency/count of the word with a set
       frequency_string = str(frequency)          # column length for word and frequency.
       print(word.ljust(20),frequency_string.rjust(4))
