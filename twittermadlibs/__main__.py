import sys
from .classifyWords import classifyWords
from .madlib import madlib
from .twitter import twitter
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

    twitterInterface = twitter()
    # We need a requestTweets option that returns a list of 3tuple usernames
    # see more info in twitter docs
    usernames = [("kanyewest", "realDonaldTrump", "12123"), ("realDonaldTrump", "kanyewest", "13313")]

    if(usernames is not None):
        for sendingUser, madlibUser, tweetID in usernames:
            generateMadlibs(sendingUser, madlibUser, tweetID, twitterInterface)


def generateMadlibs(sendingUser, madlibUser, tweetID, twitterInterface):
    # pass username to getTweets, return a list of words
    tweets = twitterInterface.get_tweets(madlibUser)

    # unique takes TextBlob object as a param, returns new textblob
    uniqueParser = unique(tweets)
    uniqueStr = uniqueParser.cleanTweets()
    # pass refinedList to parser to get a dictionary
    tweetBlob = TextBlob(uniqueStr)
    classifier = classifyWords(tweetBlob)
    tweetDict = classifier.createWordDictionary()

    # pass the dictionary to create madlibs, return a string
    madlibGenerator = madlib(tweetDict, madlibFile, preFormat, postFormat)
    madlibStr = madlibGenerator.createMadlib()

    # "@sendingUser "madlib""
    #twitterInterface.postTweet(tweet, sendingUser, madlibUser, tweetID)
    # print the string
    print(madlibStr)

if __name__ == '__main__':
    main()
