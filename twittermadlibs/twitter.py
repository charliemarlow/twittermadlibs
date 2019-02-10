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
		file = open( abs_path + "/../AccessKeysd.csv", 'r')
		reader = csv.reader(file)

		if(not os.path.exists("lastTweetID.txt")):
			lastIDFile = open(abs_path + "/lastTweetID.txt","w+")
			lastIDFile.close()
		#List order is: consumer_key, consumer_secret, access_key, access_secret
		self.keys = list(reader)

		#print(keys[0][2])  This is the access_key

		# Authorization to consumer key and consumer secret
		auth = tweepy.OAuthHandler(self.keys[0][0], self.keys[0][1])
		# Access to user's access key and access secret
		auth.set_access_token(self.keys[0][2], self.keys[0][3])

		# Calling api
		self.api = tweepy.API(auth)

	# Function to extract tweets
	def get_tweets(self, username):
		'''
		This will pull the first 100 tweets.
		'''

		# 100 tweets to be extracted
		number_of_tweets=100
		tweets = self.api.user_timeline(username,tweet_mode="extended", count= number_of_tweets)

		newListOfTweets = [tweet.full_text for tweet in tweets]
		#print(newListOfTweets)
		stringOfTweets = (" ").join(newListOfTweets)
		return stringOfTweets

	def get_profile_pic(self):
		'''
		Will return the URL to the profile picture of the username.
		:return The URL to the profile picture.
		'''
		return ("https://twitter.com/"+self.username+"/profile_image?size=original")

	def postTweet(self, tweet, sendingUser, madlibUser, tweetID):
		self.api.update_status('@' + sendingUser + " " + tweet, in_reply_to_status_id=self.tweet_)

	def getRequests(self):
		'''
		Returns a list of 3-tuples of requested tweet IDs
		(sendingUser, madlibUser, tweetID)

		Assume tweet is form  "@madlibbot1 @realDonaldTrump"
		the sending user is madlibbot1
		the at'ed user is realDonaldTrump
		remove all @s before appending to the list

		1. load last tweet id from lastTweetID.txt
		2. search for @madlibbot1
			2. save first tweet id in lastTweetID.txt
		3. for each tweet
			1. get sendingUser
			2. get the atted username
			3. get the tweets ID
			4. if the tweet ID == lastTweetID, return what's currently in the listOfTweets
			5. create 3 tuple = (sendingUser, madlibUser, tweet ID)
			6. reply_tweets.append(your_tuple)
		3. return reply_tweets
		'''


if(__name__ == '__main__'):
	twitterInterface = twitter()
	# do tests here
	twitterInterface.getRequests()
