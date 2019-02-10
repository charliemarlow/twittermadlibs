from textblob import TextBlob
import re
class unique:
    def __init__(self, tweets):
        '''
        Sets up the list of tweets for unique
        :param tweets: a string of tweets
        '''
        self.listOfTweets = tweets.split(" ")



    def cleanTweets(self):
        '''
        Cleans a tweet up, removing words smaller than 4
        and words containing links
        :return: a list of cleaned tweets
        '''
        listCopy = self.listOfTweets
        for tweet in self.listOfTweets :
            if( len(tweet) < 4 or tweet.count(".") > 0
            or tweet is None or tweet.count("@") > 0
            or tweet.count("http") > 0 or tweet.count("%") > 0
            or tweet.count("\\") > 0 or tweet.count("\/") > 0):
                listCopy.remove(tweet)

        tweetStr =  " ".join(listCopy)
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

        tweetStr = emoji_pattern.sub(r'', tweetStr)
        return tweetStr
