# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = "SOME KEY"
access_token_secret = "SOME KEY"
consumer_key = "SOME KEY"
consumer_secret = "SOME KEY"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

fn = "BaRWND!.jpeg"
stts = "Batman and Robin will never die! #UMSI-206 #UMSI206 #Proj3"

try:
	api.update_with_media(filename = fn, status = stts)
	print ("\nStatus with image and text successfully uploaded to Twitter!\n")
except:
	print ("Oh no, status was NOT uploaded!\n")