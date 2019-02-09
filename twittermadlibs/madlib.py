import csv
import random
import os

class madlib:

    def __init__(self, partsOfSpeech, madlibFile):
        self.wordsDict = partsOfSpeech
        self.file = os.path.abspath(os.path.dirname(__file__)) + madlibFile

    def getMadlib(self):
        # gets list of madlibs
        madlibs = self.readCSV()
        # gets a random entry from the list
        randomMadlib = random.choice(madlibs)
        # returns random entry
        return randomMadlib

    def createMadlib(self):

        #loop through each word
        madlib = self.getMadlib()
        wordList = madlib.split(" ")
        for i, word in enumerate(wordList):
            if(len(word) > 0 and word[0] == "#"):
                # remove hashtag from word
                oldWord = word
                word = word[1:]
                # get list of that part of speech
                partOfSpeechList = self.wordsDict[word]
                # get a random word
                word = random.choice(partOfSpeechList)
                # remove used word from the list
                partOfSpeechList.remove(word)
                wordList[i] = word


        madlib = " ".join(wordList)
        return madlib

    def readCSV(self):
        madlibs = []

        # opens file
        with open(self.file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                madlibs = madlibs + row
        madlibs = madlibs[:-1]
        madlibs = [list for list in madlibs if list is not '']
        print(madlibs)
        return madlibs
