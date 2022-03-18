import tweepy
import csv
import os


class twitter:

    def __init__(self):
        '''
        This is the constructor of the class that will take in the
        access keys.
        :param username: The Twitter handle for the user
        '''
        abs_path = os.path.abspath(os.path.dirname(__file__))
        file = open(abs_path + "/../AccessKeysd.csv", 'r')
        reader = csv.reader(file)
        self.lastTweetFile = abs_path + "/lastTweetID.txt"
        if(not os.path.exists(self.lastTweetFile)):
            lastIDFile = open(abs_path + "/lastTweetID.txt", "w+")
            lastIDFile.close()
        # List order is: consumer_key, consumer_secret, access_key, access_secret, bearer_token
        self.keys = list(reader)

        # print(keys[0][2])  This is the access_key

        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(self.keys[0][0], self.keys[0][1])
        # Access to user's access key and access secret
        auth.set_access_token(self.keys[0][2], self.keys[0][3])

        # Calling api
        self.api = tweepy.API(auth)

    # Function to extract tweets
    def getTweets(self, username):
        '''
        This will pull the first 100 tweets.
        '''

        # 100 tweets to be extracted
        number_of_tweets = 100
        stringOfTweets = None
        try:
            tweets = self.api.user_timeline(
                screen_name=username, tweet_mode="extended", count=number_of_tweets)
            newListOfTweets = [tweet.full_text for tweet in tweets]
            # print(newListOfTweets)
            stringOfTweets = (" ").join(newListOfTweets)
        except Exception as e:
            print("Tweepy error calling user_timeline: " + str(e))

        return stringOfTweets

    def getProfilePic(self, username):
        '''
        Will return the URL to the profile picture of the username.
        :return The URL to the profile picture.
        '''
        return ("https://twitter.com/"+username+"/profile_image?size=original")

    def postTweet(self, tweet, sendingUser, madlibUser, tweetID):
        '''
        Posts a tweet for the bot
        '''

        finalTweet = "@" + sendingUser + " " + \
            tweet + " (src: " + "@" + madlibUser + ")"
        try:
            self.api.update_status(finalTweet, in_reply_to_status_id=tweetID)
        except Exception as e:
            print("Tweepy error updating status: " + str(e))

    def getRequests(self):
        '''
        Returns a list of 3-tuples of requested tweet IDs
        (sendingUser, madlibUser, tweetID)

        Assume tweet is form  "@BotLibz @realDonaldTrump"
        the sending user is BotLibz
        the madlib user is realDonaldTrump
        remove all @s before appending to the list

        1. load last tweet id from lastTweetID.txt
        2. search for @BotLibz
            2. save first tweet id in lastTweetID.txt
        3. for each tweet
            1. get sendingUser
            2. get the madblib username
            3. get the tweets ID
            4. if the tweet ID == lastTweetID, return what's currently in the listOfTweets
            5. create 3 tuple = (sendingUser, madlibUser, tweet ID)
            6. reply_tweets.append(your_tuple)
        3. return reply_tweets

        :return: a list of 3-tuples
        '''
        tuples = []
        lastTweetID = self.getLastTweetID()
        query = "@BotLibz"
        print("Attempting")
        # load tweets addressed to the bot
        try:
            requests = self.api.search_tweets(q=query, count=100)
        except Exception as e:

            print("tweepy error in search: " + str(e))

        if(requests is not None and len(requests) is not 0):
            # get tweet id, set new last id
            newTweetID = requests[0]._json['id']
            self.setLastTweetID(newTweetID)

            for tweet in requests:
                # get current ID, sending user, and madlibUser
                tweetID = tweet._json['id']
                text = tweet._json['text']
                sendingUser = tweet._json['user']['screen_name']
                textList = text.split(" ")

                if(len(textList) > 1):
                    madlibUser = textList[1][1:]
                else:
                    print("error with tweet")
                    return None

                # stop if you reach the last tweet replied to
                if(tweetID == lastTweetID):
                    return tuples
                # append tuple to usernames list
                tuples.append((sendingUser, madlibUser, tweetID))
        return tuples

    def getLastTweetID(self):
        '''
        Gets the last tweet ID stored in the lastTweetFile
        :return: the last tweet ID as an int
        '''
        file = open(self.lastTweetFile, 'r')
        id = file.read()
        file.close()
        id = id.strip(" ")
        id = id.strip("\n")
        if(id is not None and id is not ''):
            id = int(id)
        return id

    def setLastTweetID(self, id):
        '''
        Erases the lastTweetFile
        Makes a new one to store the new last tweet ID
        :param id: an int ID to be stored
        '''
        os.remove(self.lastTweetFile)
        file = open(self.lastTweetFile, 'w')
        file.write(str(id))
        file.close()


# testing
if(__name__ == '__main__'):
    twitterInterface = twitter()
    # do tests here
    twitterInterface.getRequests()
