import sys
from .classifyWords import classifyWords
#from .madlib import madlib
#from .pullTweets import pullTweets
#from .unique import unique
from textblob import TextBlob

madlibFile = "../Madlibs_Template/test.csv"

def main():
    print("in main")

    # get username
    print("Enter a twitter username, no @")
    username = input()
    print("username is " + username)

    # pass username to getTweets, return a list of words
    twitterInterface = pullTweets(username)
    tweets = twitterInterface.get_tweets()
    print(tweets)

    # make textblob object from tweets
    tweetBlob = TextBlob(tweets)

    # unique takes TextBlob object as a param, returns new textblob
    uniqueParser = unique(tweetBlob)
    uniqueBlob = unique.parseTweets()


    # pass refinedList to parser to get a dictionary

    classifier = classifyWords(uniqueBlob)
    tweetDict = classifier.createWordDictionary()
    print(tweetDict)

    madlibGenerator = madlib(tweetDict, madlibFile)
    madlibStr = createMadlib()
    print(madlibStr)
    # pass the dictionary to create madlibs, return a string
    # pass a string to the formatter, return an HTMLString
    # print the string


if __name__ == '__main__':
    main()
