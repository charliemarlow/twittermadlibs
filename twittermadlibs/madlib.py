import csv
import random
import os

class madlib:
    '''
    Handles getting a random madlib, and using text replacement
    to place appropiate parts of speech in the mad madlib
    '''

    def __init__(self, partsOfSpeech, madlibFile, preFormat, postFormat):
        '''
        Sets up madlib class
        :param partsOfSpeech: a dictionary containing lists of parts of speech
        :param madlibFile: the relative file location of the madlibs csv
        :param preFormat: the HTML formatting before the inserted word
        :param postFormat: the HTML formatting after the inserted word
        '''
        self.wordsDict =    partsOfSpeech
        self.file =         os.path.abspath(os.path.dirname(__file__)) + madlibFile
        self.preFormat =    preFormat
        self.postFormat =   postFormat

    def getMadlib(self):
        '''
        Returns a random mad lib from the mad libs CSV
        :return: a random mad lib as a string
        '''
        # gets list of madlibs
        madlibs = self.readCSV()
        # gets a random entry from the list
        randomMadlib = random.choice(madlibs)
        # returns random entry
        return randomMadlib

    def createMadlib(self):
        '''
        Does text replacement on a mad lib with the appropiate part of speech
        :return: an HTML formatted string representing the entire mad lib
        '''

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
                word = self.preFormat + word + self.postFormat
                wordList[i] = word


        madlib = " ".join(wordList)
        return madlib

    def readCSV(self):
        '''
        Reads each madlib from the CSV file
        Returns it as a list where each entry is a madlib
        :return: a list of madlibs
        '''
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
