import sys
from .classifyWords import classifyWords
from .madlib import madlib
from .pullTweets import pullTweets
from .unique import unique
from textblob import TextBlob

madlibFile  = "/../Madlibs_Templates/test.csv"
preFormat   = ""
postFormat  = ""

def main():
    '''
    Main driver for the twittermadlibs program
    Passes a username to pullTweets, which returns a string of words from twitter
    The string is then passed to unique which cleans the data
    The clean data is then passed into a TextBlob object
    The TextBlob is passed to classifyWords which returns a dictionary of lists
    Each list is a different part of speech
    This dictionary is then passed to madlib which returns a finished madlib string
    '''
    print("in main")
    # get username
    '''
    print("Enter a twitter username, no @")
    username = input()
    print("username is " + username)
    '''

    # pass username to getTweets, return a list of words
    twitterInterface = pullTweets("realDonaldTrump")
    tweets = twitterInterface.get_tweets()
    profileURL = twitterInterface.get_profile_pic()

    # unique takes TextBlob object as a param, returns new textblob
    uniqueParser = unique(tweets)
    uniqueStr = uniqueParser.getTweetList()
    print(uniqueStr)
    unique2 = " ".join(uniqueStr)
    # pass refinedList to parser to get a dictionary
    tweetBlob = TextBlob(unique2)
    classifier = classifyWords(tweetBlob)
    tweetDict = classifier.createWordDictionary()
    print(tweetDict)

    # pass the dictionary to create madlibs, return a string
    madlibGenerator = madlib(tweetDict, madlibFile, preFormat, postFormat)
    madlibStr = madlibGenerator.createMadlib()

    # print the string
    print(madlibStr)


if __name__ == '__main__':
    main()
