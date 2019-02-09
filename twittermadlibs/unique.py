from textblob import TextBlob

class unique:
	def __init__(self, tweets, user_args=1):
		listOfTweets = tweets.split(" ")
		for tweet in listOfTweets :
			if( tweet.len() < 3):
				 listOfTweets.remove(tweet)