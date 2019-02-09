import sys
from .classifyWords import classifyWords
#from .pullTweets import pullTweets
#from .parser import parser
from textblob import TextBlob

def main():
    print("in main")

    # get username
    '''
    print("Enter a twitter username, no @")
    username = input()
    print("username is " + username)

    # pass username to getTweets, return a list of words
    twitterInterface = pullTweets(username)
    tweets = twitterInterface.get_tweets()
    print(tweets)
    '''

    # pass list of words to unique, get refinedList
    tweets = "this is a test grateful easily very wonderful"
    # pass refinedList to parser to get a dictionary
    tweetBlob = TextBlob(tweets)
    classifier = classifyWords(tweetBlob)
    tweetDict = classifier.createWordDictionary()
    print(tweetDict)


    # pass the dictionary to create madlibs, return a string
    # pass a string to the formatter, return an HTMLString
    # print the string


if __name__ == '__main__':
    main()
