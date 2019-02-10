import tweepy
import csv
import os

class pullTweets:


	def __init__(self, username):
		'''
		This is the constructor of the class that will take in the
		access keys.
		:param username: The Twitter handle for the user
		'''
		file = open(os.path.abspath(os.path.dirname(__file__)) + "/../AccessKeysd.csv", 'r')
		reader = csv.reader(file)

		#List order is: consumer_key, consumer_secret, access_key, access_secret
		self.keys = list(reader)

		#print(keys[0][2])  This is the access_key

		self.username = username

		self.api = None

	# Function to extract tweets
	def get_tweets(self):
		'''
		This will pull the first 100 tweets.
		'''
		# Authorization to consumer key and consumer secret
		auth = tweepy.OAuthHandler(self.keys[0][0], self.keys[0][1])
		# Access to user's access key and access secret
		auth.set_access_token(self.keys[0][2], self.keys[0][3])

		# Calling api
		self.api = tweepy.API(auth)

		# 100 tweets to be extracted
		number_of_tweets=100
		tweets = self.api.user_timeline(self.username,tweet_mode="extended", count= number_of_tweets)

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
