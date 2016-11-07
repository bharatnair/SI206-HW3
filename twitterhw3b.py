# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "2370799040-SDWQddop6P3oicAe2lZiWT1yQmpIw6DkOrn7CYU"
access_token_secret = "uyDD72qv3JiBW09lIXaa5eYS1I68tiUSEGc7Cj29zPUxJ"
consumer_key = "PbskKfNjbooKTqGKGVrM4yZOk"
consumer_secret = "lcWLjLTt91IuNKG0JFOC4r7xdTf2bzzOMqOUqURImro6LGH2XT"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.search(q = 'trivandrum')
public_tweets = api.search(input("Enter a term you'd like to search on Twitter: "))

subj_sum = 0
subj_count = 0 
pol_sum = 0
pol_count = 0

# print (type(public_tweets))
print ("\n**** start ****\n")

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	subj_sum += analysis.sentiment.subjectivity
	pol_sum += analysis.sentiment.polarity
	subj_count +=1
	pol_count +=1
	print ()

print ()
if len(public_tweets) == 0:
	print ("Oops, this search term returned zero results on Twitter!")
else:
	print("Average subjectivity: " + str(subj_sum/subj_count))
	print("Average polarity: " + str(pol_sum/pol_count))
print ()

print ("\n**** end ****\n")
