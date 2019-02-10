from textblob import TextBlob

class unique:
	def __init__(self, tweets, user_args=1):
		self.listOfTweets = tweets.split(" ")


	def cleanTweets(self):
		listCopy = self.listOfTweets
		for tweet in self.listOfTweets :
			if( len(tweet) < 4 or "." in tweet
			or tweet is None or "\\" in tweet or
			"\/" in tweet):
				listCopy.remove(tweet)

		return listCopy

	def getTweetList(self):
		return self.cleanTweets()
