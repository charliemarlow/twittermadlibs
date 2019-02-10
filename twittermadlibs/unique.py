from textblob import TextBlob

class unique:
	def __init__(self, tweets, user_args=1):
		self.listOfTweets = tweets.split(" ")
		for tweet in self.listOfTweets :
			if( len(tweet) < 4):
				self.listOfTweets.remove(tweet)

	def getTweetList(self):
		return self.listOfTweets
