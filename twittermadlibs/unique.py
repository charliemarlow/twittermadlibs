from textblob import TextBlob
import re

class unique:
    def __init__(self, tweets):
        '''
        Sets up the list of tweets for unique
        :param tweets: a string of tweets
        '''
        self.stringOfTweets = tweets
        self.listOfTweets = tweets.split(" ")

    def isInvalid(self, tweet):
        invalidLength   = len(tweet) < 4
        invalidChars    = (tweet.count(".") > 0 or tweet.count("@") > 0
                            or tweet.count("%") > 0 or tweet.count("\"") > 0
                            or tweet.count("\'") > 0 or tweet.count("\'") > 0
                            or tweet.count("\"") > 0 or tweet.count("\;") > 0
                            or tweet.count("\’") > 0 )
        invalidURL      = (tweet.count("http") > 0 or tweet.count("\\") > 0
                            or tweet.count("https") > 0 or tweet.count("\/") > 0)
        return (invalidLength or invalidChars or invalidURL)


    def cleanTweets(self):
        '''
        Cleans a tweet up, removing words smaller than 4
        and words containing links
        :return: a list of cleaned tweets
        '''
        emoji_pattern = re.compile("["
                       u"\U0001F600-\U0001F64F"  # emoticons
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       u"\U000024C2-\U0001F251"
                       u"\U0001f926-\U0001f937"
                       u"\u200d"
                       u"\u2640-\u2642"
                       "]+", flags=re.UNICODE)

        tweetsString = emoji_pattern.sub(r'', self.stringOfTweets)
        listCopy = [tweet.strip(" ") for tweet in tweetsString.split(" ")]
        listCopy2 = [tweet for tweet in listCopy if (not self.isInvalid(tweet) and tweet is not None) ]
        tweetStr =  " ".join(listCopy2)

        return tweetStr
