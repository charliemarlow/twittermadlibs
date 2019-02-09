import csv
import random

class madlib:

    def __init__(self, partsOfSpeech, madlibFile):
        self.wordsDict = partsOfSpeech
        self.file = madLibFile

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
        for word in madlib.split(" "):
            if(word[0] == "#"):
                word = word[1:-1]



    def readCSV(self):
        madlibs = []

        # opens file
        with open(self.file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                madlibs.append(row)

        return madlibs



# read CSV as a list
# choose list.random() to getMadlib
# for each word in string, if word[0] = # then parse it
# return the madLib as a string
