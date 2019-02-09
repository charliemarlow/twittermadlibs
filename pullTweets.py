import tweepy
import csv

class pullTweets:


	def __init__(self, username, user_arg=-1):
	'''
	This is the constructor of the class that will take in the
	access keys.
	:param username: The Twitter handle for the user
	'''
		file = open("AccessKeysd.csv", 'r')
		reader = csv.reader(file)
		
		#List order is: consumer_key, consumer_secret, access_key, access_secret
		keys = list(reader)
		
		#print(keys[0][2])  This is the access_key
		
		self.username = username
		
	# Function to extract tweets 
	def get_tweets():
		'''
		This will pull the first 100 tweets.
		'''
		# Authorization to consumer key and consumer secret 
	    auth = tweepy.OAuthHandler(keys[0][0], keys[0][1]) 

	    # Access to user's access key and access secret 
	    auth.set_access_token(keys[0][2], keys[0][3]) 

	    # Calling api 
	    api = tweepy.API(auth) 

	    # 200 tweets to be extracted 
	    number_of_tweets=200
	    tweets = api.user_timeline(screen_name=username) 

	    # Empty Array 
	    tmp=[]  

	    # create array of tweet information: username,  
	    # tweet id, date/time, text 
	    tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
	    for j in tweets_for_csv: 

	        # Appending tweets to the empty array tmp 
	        tmp.append(j)  

	    # Printing the tweets 
	    print(tmp) 

	
		
print("Hello")
x = SeekOutObtainAndFormatStringsAsAList("Whopper")