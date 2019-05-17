# Importing Libraries
import tweepy
from textblob import TextBlob

# Keys and Tokens
consumer_key = 'XxxxxxxxxxxxxxxxxxxxxxxxX'
consumer_secret = 'XxxxxxxxxxxxxxxxxxxxX'
access_token ='XxxxxxxxxxxxxxxxxxxxxxxxX'
access_token_secret = 'XxxxxxxxxxxxxxxxxxxX'

# Authenticating Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Searching For a Subject
public_tweets = api.search('Artificial Intelligence')
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
