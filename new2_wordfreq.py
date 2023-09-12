def tokenize(lines):  # We define a function that adds an element (word, digit or symbol)
    words = []        # to the list "words"
    for line in lines:
        start = 0
        while start < len(line):   
            while start < len(line) and line[start].isspace():  # If there is a space, start increments
                start = start + 1                               # so we avoid empty spaces.

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

def countWords(words, stopwords):
    dict = {}
    file = open("eng_stopwords.txt")
    stopwords = file.readlines()
    file.close()
    count = 0
    for i in range (0,len(words)):
        if words[i] in stopwords:
            i += 1    

        else:
        #words[i] not in stopwords:
          # count = 1
           #dict.setdefault(words[i],count)
           dict[words[i]] = dict.get(words[i],0) + 1

       # elif words[i] in dict:
       #     dict[words[i]] = dict.get(words[i],count)+1
    return dict

def freq(key_value):
    return key_value[1]

def printTopMost(dict,n):
    items = list(dict.keys())
    items.sort(key=freq, reverse = True)
    for i in range (n):
        word, frequency = items[i]
        print(word.ljust(20),frequency.rjust(5))

print(tokenize(['10. Apple, 10 sweet hello']))
