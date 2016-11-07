# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = "2370799040-SDWQddop6P3oicAe2lZiWT1yQmpIw6DkOrn7CYU"
access_token_secret = "uyDD72qv3JiBW09lIXaa5eYS1I68tiUSEGc7Cj29zPUxJ"
consumer_key = "PbskKfNjbooKTqGKGVrM4yZOk"
consumer_secret = "lcWLjLTt91IuNKG0JFOC4r7xdTf2bzzOMqOUqURImro6LGH2XT"

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