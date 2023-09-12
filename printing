dict = {"apa": 2, "monkey": 3, "car": 5, "apple": 1}

def freq(key_value):
    return key_value[1]

def printTopMost(dict,n):
    dictitems = list(dict.items())
    dictitems.sort()
    dictitems.sort(key=freq, reverse = True)
    # sorted(dictitems, key=lambda x: x[-1])
    for i in range (n):
        word, frequency = dictitems[i]
        frequency_string = str(frequency)
        print(word.ljust(20),frequency_string.rjust(5))

printTopMost(dict,3)
