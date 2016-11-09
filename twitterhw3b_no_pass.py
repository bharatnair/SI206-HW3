# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

print ()
print ("*** SI 206 - HW 3 - Twitter (B) Program (Search tweets with a term and conduct sentiment analysis) ***")
print ("\nName: Bharat Nair\nUniqname: bnair")

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "SOME KEY"
access_token_secret = "SOME KEY"
consumer_key = "SOME KEY"
consumer_secret = "SOME KEY"

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
print ("\n*^*^*\n")

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	# print(analysis.sentiment)
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

print ("\n*_*_*\n")
