import wordfreq
import sys 
import urllib.request



def main():

    if sys.argv[2].startswith("http://" or "https://"):
        response = urllib.request.urlopen(sys.argv[2])
        words = wordfreq.tokenize(response.read().decode("utf8").splitlines())
    else:
        file_toRead = open(sys.argv[2])
        words = wordfreq.tokenize(file_toRead)

    stopwordsfile = open(sys.argv[1], encoding="utf-8")
    stopwords = stopwordsfile.readlines()
    for i in range(0,len(stopwords)):
        stopwords[i] = stopwords[i].strip("\n")

    frequencyDict = wordfreq.countWords(words, stopwords)
 

    elements_toCount = int(sys.argv[3])
   
    wordfreq.printTopMost(frequencyDict, elements_toCount)

    stopwordsfile.close()
    
main()

