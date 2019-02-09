import sys
from .classifyWords import classifyWords
from textblob import TextBlob

def main():
    print("in main")

    # get username
    print("Enter a twitter username, no @")
    username = input()

    
    # pass username to getTweets, return a list of words
    # pass list of words to unique, get refinedList
    test = TextBlob("Wow. Um. Ok? You couldn't have more wholesome more say to way to say that? Bad words have no more common to make you funny! STOP curse words, block your F word or im downvoting! Cursing makes the bottom of the line: the lowest of class! People like you act like sin is all fun an game, but all they do is make me more mad!")
    classifier = classifyWords(test)
    test2 = classifier.createWordDictionary()
    print(test2)
    # pass refinedList to parser to get a dictionary
    # pass the dictionary to create madlibs, return a string
    # pass a string to the formatter, return an HTMLString
    # print the string


if __name__ == '__main__':
    main()
