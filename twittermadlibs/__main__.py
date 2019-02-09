import sys
from .classifyWords import classifyWords
from .madlib import madlib
from .pullTweets import pullTweets
#from .unique import unique
from textblob import TextBlob

madlibFile = "/../Madlibs_Templates/test.csv"

def main():
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
    # unique takes TextBlob object as a param, returns new textblob
    uniqueParser = unique(tweets)

    uniqueStr = unique.parseTweets()
    print(uniqueStr)
    unique2 = " ".join(uniqueStr)
    # pass refinedList to parser to get a dictionary
    tweetBlob = TextBlob(unique2)
    classifier = classifyWords(tweetBlob)
    tweetDict = classifier.createWordDictionary()
    print(tweetDict)

    # pass the dictionary to create madlibs, return a string
    madlibGenerator = madlib(tweetDict, madlibFile)
    madlibStr = madlibGenerator.createMadlib()
    # pass a string to the formatter, return an HTMLString
    # print the string


if __name__ == '__main__':
    main()
